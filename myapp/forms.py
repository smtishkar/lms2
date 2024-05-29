from django import forms
from .models import Certification_appointment,Dealers,Edu_programs


class CertificationAppointmentForm(forms.ModelForm):

    # dlr = forms.CharField(label='Название дилерского центра', max_length=100)
    # employee_id = forms.CharField(label='ID сотрудника', max_length=100)
    # employee_name = forms.CharField(label='Имя сотрудника', max_length=100)
    # employee_last_name = forms.CharField(label='Фамилия сотрудника', max_length=100)
    # category = forms.ModelChoiceField(label='Выберите категорию', queryset=Category.objects.all())        ## Оставил как пример списка | empty_label

    dlr = forms.ModelChoiceField(queryset=Dealers.objects.all(), empty_label='Дилер не выбран', label='Дилерский центр')
    employee_id = forms.CharField(label='ID сотрудника', max_length=100)
    level = forms.ModelChoiceField(queryset=Edu_programs.objects.all(),empty_label='Уровень не выбран', label='Уровень сертификации')
    class Meta:
        model = Certification_appointment
        # fields = ['job_title', 'certification_date', 'certification_time', 'dlr', 'employee_id', 'employee_name', 'employee_last_name']
        fields = ['dlr', 'employee_id', 'employee_name', 'employee_last_name', 'level']
        labels = {'employee_id': 'ID сотрудника',
                  'employee_name': 'Имя сотрудника',
                  'employee_last_name':'Фамилия сотрудника'
                  }

        


    #     job_title = models.CharField(max_length=250)
    # certification_date = models.DateField()
    # certification_time = models.TimeField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # # slug = models.SlugField(max_length=255, unique=True, db_index=True)
    # is_published = models.BooleanField(default=0)
    # dlr=models.CharField(max_length=250,null=True)
    # employee_id = models.CharField(max_length=250, null=True)
    # employee_name = models.CharField(max_length=250, null=True)
    # employee_last_name = models.CharField(max_length=250, null=True)
    # is_available = models.BooleanField(default=1)
