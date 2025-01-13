from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
from django.urls import reverse
from embed_video.fields import EmbedVideoField
from django.utils.text import slugify
import datetime as dt
from users.models import User


def translate_to_eng (s:str) -> str:
    d = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
    'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
    'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
    'ц':'c','ч':'ch','ш':'sh','щ':'sch','ъ':'','ы':'y','ь':'','э':'e',
    'ю':'u','я':'ya', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'YO',
    'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
    'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
    'Ц':'C','Ч':'CH','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
    'Ю':'U','Я':'YA',',':'','?':'',' ':'_','~':'','!':'','@':'','#':'',
    '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
    ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
    '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
    'Є':'e', '—':''}
    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))



class Videos(models.Model):
    video = EmbedVideoField()


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator (allowed_extensions=['mp4'])]
    )
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title




class Job_titles(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=250)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('appointment', kwargs={'app_id': self.slug})          ## Наверное тут надо что-то поменять

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.title))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "06. Список должностей"
        verbose_name_plural = "06. Список должностей"




class Site_sections(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'


    section_name = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    button_name = models.CharField(max_length=100, verbose_name='Название кнопки')
    image = models.ImageField(upload_to='static/myapp/image/', null=True, blank=True)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="Slug")
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    def __str__(self):
        return self.section_name
        
    def get_absolute_url(self):
        return reverse('part', kwargs={'part_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.section_name))

        super().save(*args, **kwargs)
    

    class Meta:
        verbose_name = "01. Разделы сайта"
        verbose_name_plural = "01. Разделы сайта"


class Technicians_cources(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'


    edu_area_name = models.CharField(max_length=100)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    button_name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='images/', null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    area = models.CharField(max_length=250)

    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    class Meta:
        verbose_name = "02. Направления обучения"
        verbose_name_plural = "02. Направления обучения"


    def __str__(self):
        return self.edu_area_name
    
    
    def get_absolute_url(self):
        return reverse('part', kwargs={'part_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.edu_area_name))

        super().save(*args, **kwargs)



class Training_parts(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    program_name = models.CharField(max_length=250)                        ## это и есть chapter поэтому поле chapte не нужно

    edu_area_name = models.CharField(max_length=250, null=True, blank=True)

    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    class Meta:
        verbose_name = "03. Содержание программы обучения"
        verbose_name_plural = "03. Содержание программы обучения"

    def __str__(self):
        return self.program_name

    def get_absolute_url(self):
        return reverse('content', kwargs={'content_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.program_name))
        super().save(*args, **kwargs)


class Training_chapters(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'


    chapter_name = models.CharField(max_length=250)

    program_name = models.CharField(max_length=250)

    description = models.TextField()

    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    class Meta:
        verbose_name = "04. Содержание конкретной программы обучения"
        verbose_name_plural = "04. Содержание конкретной программы обучения"

    def __str__(self):
        return self.chapter_name

    def get_absolute_url(self):
        return reverse('content', kwargs={'content_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.chapter_name))
        super().save(*args, **kwargs)




class Content(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'


    chapter_name = models.CharField(max_length=250)

    description = models.TextField()

    content_type = models.CharField(max_length=250)

    video = models.TextField()
    file = models.FileField(upload_to='files/', blank=True)
    slug = models.SlugField(max_length=255, db_index=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    class Meta:
        verbose_name = "05. Контенкт"
        verbose_name_plural = "05. Контент"

    def __str__(self):
        return self.chapter_name

    def get_absolute_url(self):
        return reverse('fin_content', kwargs={'fin_content_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.chapter_name))
        super().save(*args, **kwargs)














class Certification_appointment(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'


    job_title = models.CharField(max_length=250)
    certification_date = models.DateField()
    certification_time = models.TimeField(default=dt.time(00, 00))          ## Если хотим чтобы в форме был выбор установленного времени
    created_at = models.DateTimeField(auto_now_add=True)

    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")
    dlr=models.CharField(max_length=250,null=True, blank=True)
    employee_id = models.CharField(max_length=250, null=True, blank=True)
    employee_name = models.CharField(max_length=250, null=True, blank=True)
    employee_last_name = models.CharField(max_length=250, null=True, blank=True)
    level = models.CharField(max_length=250,null=True, blank=True)
    time_update = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=0)

    
    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse('appointment', kwargs={'app_id': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.job_title))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "06. Запись на сертификацию"
        verbose_name_plural = "06. Запись на сертификацию"

        ordering = ['job_title', 'certification_date', 'certification_time']





class Training_shedule(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'


    training_id = models.CharField(max_length=250, blank=True)
    training_name = models.CharField(max_length=250)
    training_start_date = models.DateField()
    training_end_date = models.DateField()
    actual_num_participants = models.IntegerField(default=0)
    max_participants = models.IntegerField()

    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")
    dlr=models.CharField(max_length=250,null=True, blank=True)
    employee_id = models.CharField(max_length=250, null=True, blank=True)
    employee_name = models.CharField(max_length=250, null=True, blank=True)
    employee_last_name = models.CharField(max_length=250, null=True, blank=True)

    is_available = models.BooleanField(default=0)

    
    def __str__(self):
        return self.training_name

    def get_absolute_url(self):
        return reverse('appointment', kwargs={'app_id': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.training_name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "08. Список тренингов"
        verbose_name_plural = "08. Список тренингов"
        ordering = ['training_name', 'training_start_date']



class Training_participants(models.Model):


    training_name = models.CharField(max_length=250)

    training_id = models.CharField(max_length=250, blank=True)
    training_start_date = models.DateField()
    training_end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    dlr=models.CharField(max_length=250,null=True, blank=True)
    employee_id = models.CharField(max_length=250, null=True, blank=True)
    employee_name = models.CharField(max_length=250, null=True, blank=True)
    employee_last_name = models.CharField(max_length=250, null=True, blank=True)


    
    def __str__(self):
        return self.training_name

    def get_absolute_url(self):
        return reverse('appointment', kwargs={'app_id': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.training_name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "06. лист участников тренинга"
        verbose_name_plural = "06. лист участников тренинга"
        ordering = ['training_name', 'training_start_date']





    
class Dealers(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=250)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('appointment', kwargs={'app_id': self.slug})          ## Наверное тут надо что-то поменять

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.title))
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "07. Список дилеров"
        verbose_name_plural = "07. Список дилеров"


class Edu_programs(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=250)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")
    cert_requirements = models.CharField(max_length=250)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('appointment', kwargs={'app_id': self.slug})          ## Наверное тут надо что-то поменять

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.title))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "08. Список всех программ обучения"
        verbose_name_plural = "08. Список всех программ обучения"




class Rights_access(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    rights_title = models.CharField(max_length=250)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    def __str__(self):
        return self.rights_title
    


    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.rights_title))
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "09. Права доступа"
        verbose_name_plural = "09. Права доступа"





class Edu_Results(models.Model):


    username = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "09. Результаты изучения"
        verbose_name_plural = "09. Результаты изучения"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fin_content', kwargs={'fin_content_slug': self.slug})          ## post это имя маршрута в urls





class Cert_Results(models.Model):


    user_id = models.CharField(max_length=250)
    cerification_name = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=250)


    class Meta:
        verbose_name = "10. Результаты Сертификации"
        verbose_name_plural = "10. Результаты Сертификации"

    def __str__(self):
        return self.user_id

    def get_absolute_url(self):
        return reverse('fin_content', kwargs={'fin_content_slug': self.slug})          ## post это имя маршрута в urls

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(translate_to_eng(self.title))
    #     super().save(*args, **kwargs)
    


class Info(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=250)
    short_description = models.TextField()
    content = models.TextField()
    file = models.FileField(upload_to='files/', blank=True)
    slug = models.SlugField(max_length=255, db_index=True)    
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('info_detailes', kwargs={'info_slug': self.slug})          ## Наверное тут надо что-то поменять 

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.title))
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "11. Новости и инфо"
        verbose_name_plural = "11. Новости и инфо"


class QuesModel(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    cert_area_test = models.CharField(max_length=200,null=True)
    question = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='static/myapp/image/', null=True, blank=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    answer = models.CharField(max_length=200,null=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")
    
    def __str__(self):
        return self.question    
    
    def get_absolute_url(self):
        return reverse('quiz', kwargs={'quiz': self.slug})          ## Наверное тут надо что-то поменять 

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.question))
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "12. Тест"
        verbose_name_plural = "12. Тест"