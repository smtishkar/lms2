from django.contrib import admin
from .models import Video, Course_structures, Site_sections, Technicians_cources

# Register your models here.

from embed_video.admin import AdminVideoMixin
from .models import Videos

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Videos, MyModelAdmin)


@admin.register(Technicians_cources)
class Technicians_courcesAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

admin.site.register(Video)
admin.site.register(Course_structures)
admin.site.register(Site_sections)
# admin.site.register(Technicians_cources)