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



# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username = cd['username'], password = cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect("/")
#     else:
#         form = LoginUserForm()
#     return render(request, 'users/login.html', {'form': form})



def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))




class ProfileUser(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model = get_user_model()
    # users = User.objects.all()
    # print(users)
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {
        'title': "Профиль пользователя",
        # 'default_image': settings.DEFAULT_USER_IMAGE,
    }
    permission_required = 'users.change_user'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.request.user.pk])

    # def get_object(self, queryset=None):
    #     return self.request.user
    






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







class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"



def profile_search(request):
    # users = User.objects.all()
    # print(users)
    # n= User.objects.get(username="test1")
    # print(n.pk)
    if request.method == 'POST':
        name = request.POST.get("name", "Undefined")
        n= User.objects.get(username=name)
        # print(name)
        # name_id = users.get(id)
        # print(n)
        uri = reverse('users:profile', args=(n.pk,))
        # print(uri)
        return HttpResponseRedirect(uri)
        # return HttpResponseRedirect(reverse('users:profile_search', args=[1]))
    return render(request, 'users/profile_search.html')



