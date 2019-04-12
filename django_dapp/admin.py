from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Application, Release


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ['author', ]

    list_display = ('name', 'slug', 'author', 'display__releases_count', 'created', 'modified')
    list_select_related = ('author',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def display__releases_count(self, obj=None):
        return obj.releases.count()

    display__releases_count.short_description = _('releases count')


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    readonly_fields = ['author', 'checksum']
    list_select_related = ('application', 'author',)
    list_display = ('application', 'version', 'author', 'minimum', 'checksum', 'created', 'modified')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)
