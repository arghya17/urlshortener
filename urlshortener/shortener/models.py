from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class LongToShort(models.Model):
    long_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=50, unique=True)
    date = models.DateField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    firefox = models.IntegerField(default=0)
    chrome = models.IntegerField(default=0)
    opera = models.IntegerField(default=0)
    others = models.IntegerField(default=0)
    desktop = models.IntegerField(default=0)
    mobile = models.IntegerField(default=0)
