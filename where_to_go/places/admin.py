from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    readonly_fields = ['get_preview', ]
    fields = ['image', 'get_preview', 'number']
    model = Image

    def get_preview(self, instance):
        if instance.image:
            return format_html(
                '<img src="{url}" style="max-height: 200px; max-width: 200px;/>',
                url=instance.image.url
                )
        else:
            return format_html('<p>Здесь будет превью, когда вы выберете файл.</p>')


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)
