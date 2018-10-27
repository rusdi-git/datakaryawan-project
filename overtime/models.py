from django.db import models

# Create your models here.

class Overtime(models.Model):
    noreg = models.CharField(max_length=20)
    date_in = models.DateTimeField()
    date_out = models.DateTimeField()