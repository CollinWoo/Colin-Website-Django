from django.contrib import admin
from .models import *
from adminsortable2.admin import SortableAdminMixin

# Register your models here.
@admin.register(ProjectCard)
class ProjectCardAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ["extension", "is_img"]

    def save_model(self, request, obj, form, change):
        if 'media' in form.changed_data:
            obj.extension = obj.get_media_extension()
        super().save_model(request, obj, form, change)

    list_display = ('img_caption', 'extension')
    fieldsets = (
        ('Caption', {
            'fields': ('img_caption', 'show_caption')
        }),
        ('Background', {
            'fields': ('media', ('extension', 'is_img'))
        }),
        ('Other', {
            'fields': ('description', 'link')
        }),
    )

admin.site.register(DescriptionPage)
