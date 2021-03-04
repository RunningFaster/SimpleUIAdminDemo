from django.contrib import admin

# Register your models here.

from . import models


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        fields = [field.name for field in self.model._meta.fields]
        return fields
