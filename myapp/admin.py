from django.contrib import admin
from .models import Video, Site_sections, Technicians_cources, Training_chapters, Training_parts, Certification_appointment

# Register your models here.

from embed_video.admin import AdminVideoMixin
from .models import Videos

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Videos, MyModelAdmin)


@admin.register(Site_sections)
class Site_sectionsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Technicians_cources)
class Technicians_courcesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    # readonly_fields = ['slug']


@admin.register(Training_chapters)
class Training_chaptersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Training_parts)
class Training_partsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Certification_appointment, MyModelAdmin)


admin.site.register(Video)
# admin.site.register(Site_sections)
# admin.site.register(Technicians_cources)