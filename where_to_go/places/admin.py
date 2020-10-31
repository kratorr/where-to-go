from django.contrib import admin

# Register your models here.
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image

class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)
