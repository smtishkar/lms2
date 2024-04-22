from django.contrib import admin
from .models import Video, Course_structures, Site_sections, Technicians_cources

# Register your models here.


admin.site.register(Video)
admin.site.register(Course_structures)
admin.site.register(Site_sections)
admin.site.register(Technicians_cources)