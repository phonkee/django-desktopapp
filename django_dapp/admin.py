from django.contrib import admin
from django.template.loader import get_template
from django.utils.functional import cached_property
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from .models import Application, Release


class ReleaseInline(admin.StackedInline):
    model = Release
    can_delete = False
    extra = 0

    fields = ('version', 'author', 'release_notes', 'minimum')

    def get_queryset(self, request):
        return self.model.objects.order_by("version")

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ['author', ]
    list_editable = ('is_default',)
    list_display = (
        'name', 'slug', 'is_default', 'author', 'display__releases_count', 'created', 'modified', 'display__icons')
    list_select_related = ('author',)

    inlines = (ReleaseInline,)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def display__releases_count(self, obj=None):
        return obj.releases.count()

    display__releases_count.short_description = _('releases count')

    @cached_property
    def icons_template(self):
        return get_template("django_dapp/application_actions.html")

    def display__icons(self, obj=None):
        return format_html(self.icons_template.render({
            "application": obj
        }))

    display__icons.short_description = _('actions')


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_select_related = ('application', 'author',)
    list_display = ('__str__', 'application', 'author', 'minimum', 'checksum', 'created', 'modified')
    list_editable = ('minimum',)
    raw_id_fields = ('application',)

    class Media:
        css = {
            'all': ('codemirror/lib/codemirror.css',)
        }
        js = ('codemirror/lib/codemirror.js', 'codemirror/mode/markdown/markdown.js', 'js/django_dapp_cm.js')

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = ['author', 'checksum']

        if obj is not None:
            readonly_fields.append('application')

        return readonly_fields

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)
