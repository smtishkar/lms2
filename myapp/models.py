from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
from embed_video.fields import EmbedVideoField

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


class Course_structures(models.Model):
    title = models.CharField(max_length=100)
    chaper = models.CharField(max_length=100)
    section = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title



class Site_sections(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    button_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/myapp/image/')

    def __str__(self):
        return self.title
    
class Technicians_cources(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    button_name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='static/myapp/image/')
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=100)


    
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

    def get_absolute_url(self):
        return reverse('post', kwargs={'section_slug': self.slug})

    def save(self, *args, **kwargs):
        # self.slug = translate_to_eng(self.title)
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)