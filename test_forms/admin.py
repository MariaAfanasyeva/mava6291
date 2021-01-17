from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.InputModel)
class InputAdmin(admin.ModelAdmin):
    list_display = ('field', 'data',)
