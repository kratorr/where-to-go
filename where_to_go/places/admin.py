from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    readonly_fields = ('get_preview', )
    fields = ('image', 'get_preview', 'number')
    model = Image

    def get_preview(self, obj):
        width = obj.image.width
        height = obj.image.height
        max_width = 200
        max_height = 200
        if width > max_width:
            ratio = max_width / width
            height = height * ratio
            width = width * ratio
        elif height > max_height:
            ratio = max_height / height
            width = width * ratio
            height = height * ratio
        else:
            width = max_width
            height = max_height
        return format_html('<img src="{url}" width={width} height={height} />'.format(
            url=obj.image.url,
            width=width,
            height=height
            )
        )


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)
