# Register your models here.

from django.contrib import admin
from django.utils.html import format_html
from .models import Seed, Patch


class ReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Seed)
class SeedAdmin(ReadOnlyAdmin):
    readonly_fields = ('generated', 'permalink')
    list_display = ('id', 'seed', 'generated', 'permalink')
    ordering = ('-generated',)

    # Custom field for permalink to seed.
    @admin.display(description="Permalink")
    def permalink(self, obj: Seed) -> str:
        return format_html('<a href="{}" target="_blank">Permalink</a>', obj.permalink)


@admin.register(Patch)
class PatchAdmin(ReadOnlyAdmin):
    readonly_fields = ('generated', 'permalink')
    list_display = ('id', 'seed', 'generated', 'permalink')
    ordering = ('-generated',)

    # Custom field for permalink to patch.
    @admin.display(description="Permalink")
    def permalink(self, obj: Patch) -> str:
        return format_html('<a href="{}" target="_blank">Permalink</a>', obj.permalink)
