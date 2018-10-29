from django.db import models

# Create your models here.

class Overtime(models.Model):
    noreg = models.CharField(max_length=20)
    date_in = models.DateTimeField(null=True, blank=True)
    date_out = models.DateTimeField(null=True, blank=True)