from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
from django.urls import reverse
from embed_video.fields import EmbedVideoField
from django.utils.text import slugify
import datetime as dt


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


class Site_sections(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'


    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    button_name = models.CharField(max_length=100, verbose_name='Название кнопки')
    image = models.ImageField(upload_to='static/myapp/image/')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="Slug")
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('part', kwargs={'part_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.title))
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

    class Meta:
        verbose_name = "1. Разделы сайта"
        verbose_name_plural = "1. Разделы сайта"


class Technicians_cources(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'


    title = models.CharField(max_length=100)
    description = models.TextField()
    button_name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='static/myapp/image/')
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    job_title = models.CharField(max_length=250)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    class Meta:
        verbose_name = "2. Программы обучения"
        verbose_name_plural = "2. Программы обучения"


    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('part', kwargs={'part_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.title))
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Training_parts(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=250)                        ## это и есть chapter поэтому поле chapte не нужно
    area = models.CharField(max_length=250)
    level = models.CharField(max_length=250)
    # chapter = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    class Meta:
        verbose_name = "3. Главы программы обучения"
        verbose_name_plural = "3. Главы программы обучения"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('part', kwargs={'part_slug': self.slug})          ## post это имя маршрута в urls
        return reverse('content', kwargs={'content_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.title))
        super().save(*args, **kwargs)


class Training_chapters(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'


    title = models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    level = models.CharField(max_length=250)
    chapter = models.CharField(max_length=250)
    section = models.CharField(max_length=250, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    content_type = models.CharField(max_length=250)
    video = EmbedVideoField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    class Meta:
        verbose_name = "4. Разделы глав обучения"
        verbose_name_plural = "4. Разделы глав обучения"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content', kwargs={'content_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.title))
        super().save(*args, **kwargs)




class Content(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'


    title = models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    level = models.CharField(max_length=250)
    chapter = models.CharField(max_length=250)
    section = models.CharField(max_length=250, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    content_type = models.CharField(max_length=250)
    video = EmbedVideoField(blank=True)
    slug = models.SlugField(max_length=255, db_index=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    class Meta:
        verbose_name = "5. Контенкт"
        verbose_name_plural = "5. Контент"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fin_content', kwargs={'fin_content_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.title))
        super().save(*args, **kwargs)














class Certification_appointment(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    # title = models.CharField(max_length=250)
    job_title = models.CharField(max_length=250)
    certification_date = models.DateField()
    certification_time = models.TimeField(default=dt.time(00, 00))          ## Если хотим чтобы в форме был выбор установленного времени
    created_at = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True)
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
        verbose_name = "6. Запись на сертификацию"
        verbose_name_plural = "6. Запись на сертификацию"
        # ordering = ['-time_create']
        ordering = ['job_title', 'certification_date', 'certification_time']
        # indexes = [
        #     models.Index(fields=['-time_create'])
        # ]




class Training_shedule(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    # title = models.CharField(max_length=250)
    training_id = models.CharField(max_length=250, blank=True)
    training_name = models.CharField(max_length=250)
    training_start_date = models.DateField()
    training_end_date = models.DateField()
    actual_num_participants = models.IntegerField(default=0)
    max_participants = models.IntegerField()
    # slug = models.SlugField(max_length=255, unique=True, db_index=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")
    dlr=models.CharField(max_length=250,null=True, blank=True)
    employee_id = models.CharField(max_length=250, null=True, blank=True)
    employee_name = models.CharField(max_length=250, null=True, blank=True)
    employee_last_name = models.CharField(max_length=250, null=True, blank=True)
    # time_update = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=0)

    
    def __str__(self):
        return self.training_name

    def get_absolute_url(self):
        return reverse('appointment', kwargs={'app_id': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.training_name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "6. Запись на тренинги"
        verbose_name_plural = "6. Запись на тренинги"
        ordering = ['training_name', 'training_start_date']



class Training_participants(models.Model):

    # class Status(models.IntegerChoices):
    #     DRAFT = 0, 'Черновик'
    #     PUBLISHED = 1, 'Опубликовано'

    # title = models.CharField(max_length=250)
    training_name = models.CharField(max_length=250)
    # training_id = models.ForeignKey(Training_shedule,on_delete=models.DO_NOTHING)
    training_id = models.CharField(max_length=250, blank=True)
    training_start_date = models.DateField()
    training_end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    # actual_num_participants = models.IntegerField(default=0)
    # max_participants = models.IntegerField()
    # slug = models.SlugField(max_length=255, unique=True, db_index=True)
    # is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
    #                                    default=Status.DRAFT, verbose_name="Статус")
    dlr=models.CharField(max_length=250,null=True, blank=True)
    employee_id = models.CharField(max_length=250, null=True, blank=True)
    employee_name = models.CharField(max_length=250, null=True, blank=True)
    employee_last_name = models.CharField(max_length=250, null=True, blank=True)
    # time_update = models.DateTimeField(auto_now=True)
    # is_available = models.BooleanField(default=0)

    
    def __str__(self):
        return self.training_name

    def get_absolute_url(self):
        return reverse('appointment', kwargs={'app_id': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.training_name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "6. лист участников тренинга"
        verbose_name_plural = "6. лист участников тренинга"
        ordering = ['training_name', 'training_start_date']





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
        verbose_name = "6. Список должностей"
        verbose_name_plural = "6. Список должностей"

    
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
        verbose_name = "7. Список дилеров"
        verbose_name_plural = "7. Список дилеров"


class Edu_programs(models.Model):

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
        verbose_name = "8. Список всех программ обучения"
        verbose_name_plural = "8. Список всех программ обучения"




class Rights_access(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    rights_title = models.CharField(max_length=250)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")

    def __str__(self):
        return self.rights_title
    
    # def get_absolute_url(self):
    #     return reverse('appointment', kwargs={'app_id': self.slug})          ## Наверное тут надо что-то поменять

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.rights_title))
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "9. Права доступа"
        verbose_name_plural = "9. Права доступа"