from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


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
    image = models.ImageField(upload_to='static/myapp/image/')