from django.contrib import admin
from . import models


@admin.register(models.Book)
class CustomBookAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Metadata)
class CustomMetadataAdmin(admin.ModelAdmin):
    pass
