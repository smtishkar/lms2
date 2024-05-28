from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
from django.urls import reverse
from embed_video.fields import EmbedVideoField
from django.utils.text import slugify


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
    title = models.CharField(max_length=100)
    description = models.TextField()
    button_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/myapp/image/')
    slug = models.SlugField(max_length=255, db_index=True)
    is_published = models.BooleanField(default=0)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('part', kwargs={'part_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.title))
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

class Technicians_cources(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    button_name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='static/myapp/image/')
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    job_title = models.CharField(max_length=250)
    is_published = models.BooleanField(default=0)

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('part', kwargs={'part_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.title))
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Training_parts(models.Model):
    title = models.CharField(max_length=250)                        ## это и есть chapter поэтому поле chapte не нужно
    area = models.CharField(max_length=250)
    level = models.CharField(max_length=250)
    # chapter = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    is_published = models.BooleanField(default=0)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('part', kwargs={'part_slug': self.slug})          ## post это имя маршрута в urls
        return reverse('content', kwargs={'content_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.title))
        super().save(*args, **kwargs)


class Training_chapters(models.Model):
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
    is_published = models.BooleanField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content', kwargs={'content_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.title))
        super().save(*args, **kwargs)


class Certification_appointment(models.Model):
    # title = models.CharField(max_length=250)
    job_title = models.CharField(max_length=250)
    certification_date = models.DateField()
    certification_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True)
    is_published = models.BooleanField(default=0)
    dlr=models.CharField(max_length=250,null=True)
    employee_id = models.CharField(max_length=250, null=True)
    employee_name = models.CharField(max_length=250, null=True)
    employee_last_name = models.CharField(max_length=250, null=True)
    is_available = models.BooleanField(default=1)

    
    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse('content', kwargs={'content_slug': self.slug})          ## post это имя маршрута в urls

    def save(self, *args, **kwargs):
        self.slug = slugify(translate_to_eng(self.job_title))
        super().save(*args, **kwargs)