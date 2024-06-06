from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginUserForm
from django.views.generic import CreateView, UpdateView
from .forms import LoginUserForm, RegisterUserForm

# Create your views here.

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extrac_context = {'title': 'Авторизация'}


    def get_success_url(self) -> str:
        return reverse_lazy('index')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:login')


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