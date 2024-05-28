from django import forms
# from .models import Category, User


class CertificationAppointmentForm(forms.Form):
    dlr = forms.CharField(label='Название дилерского центра', max_length=100)
    employee_id = forms.CharField(label='ID сотрудника', max_length=100)
    employee_name = forms.CharField(label='Имя сотрудника', max_length=100)
    employee_last_name = forms.CharField(label='Фамилия сотрудника', max_length=100)
    # category = forms.ModelChoiceField(label='Выберите категорию', queryset=Category.objects.all())        ## Оставил как пример списка | empty_label