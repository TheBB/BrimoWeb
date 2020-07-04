from django.contrib import admin

from . import models


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('name', 'imagefile', 'image_tag',)
    readonly_fields = ('image_tag',)


@admin.register(models.Juxtaposition)
class JuxtapositionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    pass
