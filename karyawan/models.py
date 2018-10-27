from django.db import models

# Create your models here.
class Karyawan(models.Model):
    noreg = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=150, null=True, blank=True)