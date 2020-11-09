from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    readonly_fields = ['get_preview', ]
    fields = ['image', 'get_preview', 'number']
    model = Image

    def get_preview(self, obj):

        return format_html(
            '<img src="{url}"} />'.format(
                url=obj.image.url
            )
        )


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)
