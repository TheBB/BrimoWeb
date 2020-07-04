from django.contrib import admin

from .models import Image, Juxtaposition


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('name', 'imagefile', 'image_tag',)
    readonly_fields = ('image_tag',)


@admin.register(Juxtaposition)
class JuxtapositionAdmin(admin.ModelAdmin):
    fields = ('name', 'before', 'after')
