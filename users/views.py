from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginUserForm, UserPasswordChangeForm
from django.views.generic import CreateView, UpdateView
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserProfileSearhForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin


from csv import DictReader
from io import TextIOWrapper

# Create your views here.

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extrac_context = {'title': 'Авторизация'}


    def get_success_url(self) -> str:
        return reverse_lazy('index')


class RegisterUser(PermissionRequiredMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:login')
    permission_required = 'users.add_user'




def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))




class ProfileUser(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model = get_user_model()

    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {
        'title': "Профиль пользователя",

    }
    permission_required = 'users.change_user'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.request.user.pk])


    






# class ProfileUser(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
#     model = get_user_model()
#     form_class = ProfileUserForm
#     template_name = 'users/profile.html'
#     extra_context = {
#         'title': "Профиль пользователя",
#         # 'default_image': settings.DEFAULT_USER_IMAGE,
#     }
#     permission_required = 'users.change_user'

#     def get_success_url(self):
#         return reverse_lazy('users:profile')

#     def get_object(self, queryset=None):
#         return self.request.user







class UserPasswordChange(PermissionRequiredMixin, PasswordChangeView):
    model = get_user_model()
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
    permission_required = 'users.change_user'

    def get_form_kwargs(self,*args, **kwargs):
        pk = self.kwargs.get('pk')
        print(pk)
        kwargs = super().get_form_kwargs()
        kwargs['user'] = User.objects.get(id=pk)  # or any, or get id from url
        print(kwargs)
        return kwargs


    # def password_change(request):


    #     name = 
    #     user=User.objects.get(username=name)
    #     form_class = self.get_form_class()
    #     form = form_class(user=user)

    #     return self.render_to_response(self.get_context_data())

    
    def get_success_url(self):
        return reverse_lazy('users:password_change', args=[self.request.user.pk])
    

# def change_password(request, *args, **kwargs):

#     # name = request.POST.get("name", "Undefined")
#     n= User.objects.get(username='test1')

#     print(n.access_rights)
#     if request.method == 'POST':
#         form = UserPasswordChangeForm
#         print(n)
#         # if form.is_valid():
#     return render(request, 'users/password_change_form.html')


def profile_search(request):
    # users = User.objects.all()
    # print(users)
    # n= User.objects.get(username="test1")
    # print(n.pk)
    if request.method == 'POST':
        name = request.POST.get("name", "Undefined")
        button_name = request.POST.get('profile') or request.POST.get('password')
        n= User.objects.get(username=name)
        print(n)
        print(button_name)
        if button_name == 'profile':
            uri = reverse('users:profile', args=(n.pk,))
            return HttpResponseRedirect(uri)
        if button_name == 'password':
            uri = reverse('users:password_change', args=(n.pk,))    
        # name_id = users.get(id)
        # print(n)
        # print(uri)
            return HttpResponseRedirect(uri)
        # return HttpResponseRedirect(reverse('users:profile_search', args=[1]))
    else:
        form = ProfileUser()
    return render(request, 'users/profile_search.html')



