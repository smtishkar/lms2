from django.contrib import admin
from .models import Content, Video, Site_sections, Technicians_cources, Training_chapters, Training_parts, Certification_appointment, Job_titles, Dealers, Edu_programs, Training_shedule, Training_participants, Rights_access, Cert_Results, Info, QuesModel, Edu_Results
from django.contrib import messages

# Register your models here.

from embed_video.admin import AdminVideoMixin
from .models import Videos

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Videos, MyModelAdmin)



@admin.register(Site_sections)
class Site_sectionsAdmin(admin.ModelAdmin):
    fields = ['section_name', 'slug', 'description', 'button_name', 'image', 'is_published']
    prepopulated_fields = {'slug': ('section_name',)}
    list_display = ('id', 'section_name', 'slug', 'button_name', 'is_published')
    list_display_links = ('section_name', )    
    ordering = ['id']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['section_name']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Site_sections.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Site_sections.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


@admin.register(Technicians_cources)
class Technicians_courcesAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']

    fields = ['edu_area_name', 'slug', 'description', 'button_name', 'image', 'area', 'is_published']
    prepopulated_fields = {'slug': ('edu_area_name',)}
    list_display = ('id', 'edu_area_name', 'slug', 'button_name', 'area', 'is_published')
    list_display_links = ('edu_area_name', )    
    ordering = ['id']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['edu_area_name']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Technicians_cources.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Technicians_cources.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)



@admin.register(Training_parts)
class Training_partsAdmin(admin.ModelAdmin):
    fields = ['program_name', 'slug', 'description', 'edu_area_name', 'image', 'is_published']
    prepopulated_fields = {'slug': ('program_name',)}
    list_display = ('id', 'program_name', 'slug',  'edu_area_name', 'is_published')
    list_display_links = ('program_name', )    
    ordering = ['id']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['program_name']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Training_parts.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Training_parts.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)



@admin.register(Training_chapters)
class Training_chaptersAdmin(admin.ModelAdmin):
    fields = ['chapter_name', 'slug', 'description', 'program_name', 'is_published']
    prepopulated_fields = {'slug': ('chapter_name',)}
    list_display = ('id', 'chapter_name', 'slug', 'program_name',  'is_published')
    list_display_links = ('chapter_name', )    
    ordering = ['id']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['chapter_name']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Training_chapters.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Training_chapters.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    fields = ['chapter_name', 'slug', 'description','content_type', 'video', 'file', 'is_published']
    prepopulated_fields = {'slug': ('chapter_name',)}
    list_display = ('id', 'chapter_name', 'slug', 'content_type', 'is_published')
    list_display_links = ('chapter_name', )    
    ordering = ['id']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['chapter_name']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Training_chapters.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Training_chapters.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)







@admin.register(Certification_appointment)
class Certification_appointmentAdmin(admin.ModelAdmin):
    fields = ['job_title', 'certification_date', 'certification_time', 'is_published', 'dlr', 'employee_id', 'employee_name', 'employee_last_name', 'level', 'is_available']
    list_display = ('id', 'job_title', 'certification_date', 'certification_time', 'dlr', 'employee_id','employee_name', 'employee_last_name', 'level', 'time_update','is_available', 'is_published')
    list_display_links = ('job_title', )    
    ordering = ['id']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['job_title']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Certification_appointment.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Certification_appointment.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)



@admin.register(Training_shedule)
class Training_sheduleAdmin(admin.ModelAdmin):
    fields = ['training_name', 'training_id', 'training_start_date', 'training_end_date', 'is_published', 'actual_num_participants','max_participants', 'is_available']
    list_display = ('id', 'training_name', 'training_id', 'training_start_date', 'training_end_date', 'actual_num_participants', 'max_participants', 'is_available', 'is_published')
    # fields = ['trainin_name', 'training_start_date', 'training_end_date', 'is_published', 'max_participants', 'dlr', 'employee_id', 'employee_name', 'employee_last_name', 'is_available']
    # list_display = ('id', 'trainin_name', 'training_start_date', 'training_end_date', 'max_participants', 'dlr', 'employee_id','employee_name', 'employee_last_name', 'time_update','is_available', 'is_published')
    list_display_links = ('training_name', )    
    ordering = ['id']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['training_name']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Training_shedule.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Training_shedule.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)



@admin.register(Training_participants)
class Training_participantsAdmin(admin.ModelAdmin):
    fields = ['training_name', 'training_start_date', 'training_end_date', 'dlr', 'employee_id', 'employee_name', 'employee_last_name', 'training_id']
    list_display = ('id', 'training_name', 'training_start_date', 'training_end_date', 'dlr', 'employee_id', 'employee_name', 'employee_last_name', 'training_id')
    # fields = ['trainin_name', 'training_start_date', 'training_end_date', 'is_published', 'max_participants', 'dlr', 'employee_id', 'employee_name', 'employee_last_name', 'is_available']
    # list_display = ('id', 'trainin_name', 'training_start_date', 'training_end_date', 'max_participants', 'dlr', 'employee_id','employee_name', 'employee_last_name', 'time_update','is_available', 'is_published')
    list_display_links = ('training_name', )    
    ordering = ['id']
    # list_editable = ('is_published', )
    list_per_page = 10
    # actions = ['set_published', 'set_draft']
    search_fields = ['training_name']

    # @admin.action(description="Опубликовать выбранные записи")
    # def set_published(self, request, queryset):
    #     count = queryset.update(is_published=Training_shedule.Status.PUBLISHED)
    #     self.message_user(request, f"Изменено {count} записей.")

    # @admin.action(description="Снять с публикации выбранные записи")
    # def set_draft(self, request, queryset):
    #     count = queryset.update(is_published=Training_shedule.Status.DRAFT)
    #     self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)




@admin.register(Job_titles)
class Job_titlesAdmin(admin.ModelAdmin):
    fields = ['title', 'is_published']
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('title', )    
    ordering = ['id']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['title']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Job_titles.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Job_titles.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)



@admin.register(Dealers)
class DealersAdmin(admin.ModelAdmin):
    fields = ['title', 'is_published']
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('title', )    
    ordering = ['id']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['title']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Dealers.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Dealers.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)



@admin.register(Edu_programs)
class Edu_programsAdmin(admin.ModelAdmin):
    fields = ['title', 'is_published', 'cert_requirements']
    list_display = ('id', 'title', 'cert_requirements', 'is_published')
    list_display_links = ('title', )    
    ordering = ['id']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['title']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Edu_programs.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Edu_programs.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)




@admin.register(Edu_Results)
class Edu_ResultsAdmin(admin.ModelAdmin):
    fields = ['title', 'username']
    list_display = ('id', 'title', 'username', 'create_at',)
    list_display_links = ('title', )    
    ordering = ['id']
    # list_editable = ('is_published', )
    list_per_page = 10
    # actions = ['set_published', 'set_draft']
    search_fields = ['title', 'username']

    # @admin.action(description="Опубликовать выбранные записи")
    # def set_published(self, request, queryset):
    #     count = queryset.update(is_published=Edu_programs.Status.PUBLISHED)
    #     self.message_user(request, f"Изменено {count} записей.")

    # @admin.action(description="Снять с публикации выбранные записи")
    # def set_draft(self, request, queryset):
    #     count = queryset.update(is_published=Edu_programs.Status.DRAFT)
    #     self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)



@admin.register(Rights_access)
class Rights_accessAdmin(admin.ModelAdmin):
    fields = ['rights_title', 'is_published']
    list_display = ('id', 'rights_title', 'is_published')
    list_display_links = ('rights_title', )    
    ordering = ['id']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['rights_title']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Rights_access.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Rights_access.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


@admin.register(Cert_Results)
class Certification_ResultsAdmin(admin.ModelAdmin):
    fields = ['user_id', 'cerification_name', 'status', 'score', 'cert_status']
    list_display = ('user_id', 'cerification_name', 'create_at', 'status', 'score', 'cert_status',)
    list_display_links = ('user_id', )    
    ordering = ['user_id']
    # list_editable = ('is_published', )
    list_per_page = 10
    # actions = ['set_published', 'set_draft']
    search_fields = ['user_id']

    # @admin.action(description="Опубликовать выбранные записи")
    # def set_published(self, request, queryset):
    #     count = queryset.update(is_published=Dealers.Status.PUBLISHED)
    #     self.message_user(request, f"Изменено {count} записей.")

    # @admin.action(description="Снять с публикации выбранные записи")
    # def set_draft(self, request, queryset):
    #     count = queryset.update(is_published=Dealers.Status.DRAFT)
    #     self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    fields = ['title', 'short_description','content', 'file', 'slug',  'is_published']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'short_description', 'is_published')
    list_display_links = ('title', )    
    ordering = ['id']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['title']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Rights_access.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Rights_access.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


@admin.register(QuesModel)
class QuizAdmin(admin.ModelAdmin):
    fields = ['cert_area_test', 'question', 'image', 'op1', 'op2', 'op3', 'op4', 'answer', 'is_published']
    list_display = ('id','cert_area_test', 'question', 'is_published')
    list_display_links = ('question', )    
    ordering = ['id']
    list_editable = ('is_published', )
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['question']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Dealers.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Dealers.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


admin.site.register(Video)






