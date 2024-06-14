from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from myapp.models import Dealers, Job_titles, Rights_access


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput())
    dlr = forms.ModelChoiceField(queryset=Dealers.objects.all(), empty_label='Дилер не выбран', label='Дилерский центр')
    job_title = forms.ModelChoiceField(queryset=Job_titles.objects.all(), empty_label='Должность не выбрана', label='Должность')
    job_title2 = forms.ModelChoiceField(queryset=Job_titles.objects.all(), empty_label='2ая Должность не выбрана', label='2ая должность')
    access_rights = forms.ModelChoiceField(queryset=Rights_access.objects.all(), empty_label='Права не выбраны', label='Права доступа')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'date_birth', 'dlr', 'job_title', 'job_title2', 'saba_id', 'access_rights']
        label = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }


