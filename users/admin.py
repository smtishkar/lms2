from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# admin.site.register(User, UserAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'first_name', 'last_name', 'password', 'date_birth', 'date_joined','dlr', 'job_title', 'job_title2', 'saba_id', 'access_rights', 'is_active','groups']
    # prepopulated_fields = {'slug': ('title',)}
    list_display = ('username', 'date_birth', 'dlr', 'job_title', 'job_title2', 'saba_id', 'access_rights', 'is_active')
    # list_display_links = ('title', )    
    ordering = ['id']
    # list_editable = ('is_published', )
    list_per_page = 10
    # actions = ['set_published', 'set_draft']
    # search_fields = ['title']

    # @admin.action(description="Опубликовать выбранные записи")
    # def set_published(self, request, queryset):
    #     count = queryset.update(is_published=Site_sections.Status.PUBLISHED)
    #     self.message_user(request, f"Изменено {count} записей.")

    # @admin.action(description="Снять с публикации выбранные записи")
    # def set_draft(self, request, queryset):
    #     count = queryset.update(is_published=Site_sections.Status.DRAFT)
    #     self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


  