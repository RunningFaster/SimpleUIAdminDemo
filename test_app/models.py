from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Teacher(models.Model):
    name = models.CharField("姓名", max_length=200)


class Student(models.Model):
    name = models.CharField("姓名", max_length=200)


class System(models.Model):
    LEVEL = (
        (1, "一级菜单"),
        (2, "二级菜单"),
    )
    level = models.IntegerField("等级", default=1, choices=LEVEL, blank=True)
    name = models.CharField("模块", max_length=200)


class BaseUser(AbstractUser):
    systems = models.ManyToManyField("System", through="BaseUserSystem")

    def has_perm(self, perm, obj=None):
        from django.conf import settings
        # 大模块控制
        # menu_display = settings.SIMPLEUI_CONFIG["menu_display"]
        # settings.SIMPLEUI_CONFIG["menu_display"] = menu_display[:1]
        # 内部模型控制
        # menu_display = settings.SIMPLEUI_CONFIG["menus"][0]["models"]
        # settings.SIMPLEUI_CONFIG["menus"][0]["models"] = menu_display[:1]
        # self.base_user_system
        return self.is_superuser


class BaseUserSystem(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE, related_name="base_user_system")
    base_user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name="base_user_system")
