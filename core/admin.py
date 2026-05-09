from django.contrib import admin
from .models import AboutMe, Skill, Project, Certificate, ContactMessage

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'headline', 'contact_email')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order')
    list_editable = ('order',)
    list_filter = ('category',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'live_url')
    list_editable = ('order',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'date_issued', 'order')
    list_editable = ('order',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('created_at',)
