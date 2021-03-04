from django.contrib import admin
from . import models


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        fields = [field.name for field in self.model._meta.fields]
        return fields


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        fields = [field.name for field in self.model._meta.fields]
        return fields


@admin.register(models.System)
class SystemAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        fields = [field.name for field in self.model._meta.fields]
        return fields


@admin.register(models.BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        fields = [field.name for field in self.model._meta.fields]
        return fields
