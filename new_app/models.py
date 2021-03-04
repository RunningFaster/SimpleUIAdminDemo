from django.db import models


# Create your models here.
class Class(models.Model):
    name = models.CharField("班级", max_length=200)
