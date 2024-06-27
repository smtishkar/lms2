from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordChangeView


app_name = "users"

urlpatterns = [

    path('login/', views.LoginUser.as_view(), name = 'login'),
    path('logout/', views.logout_user, name = 'logout'), 
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('password-change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password-change/done', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('profile/<int:pk>/', views.ProfileUser.as_view(), name='profile'),
    path('profile_search/', views.profile_search, name='profile_search'),
    # path('database/', views.profile_search, name='profile_search'),
]