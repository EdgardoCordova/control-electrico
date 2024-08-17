from django.db import models
from programs.models import crc_PROG
from django.utils.text import slugify


# Create your models here.
class crc_ONOFF(models.Model):
    event_hour = models.PositiveSmallIntegerField(editable=True, blank=True, null=True)
    event_minute = models.PositiveSmallIntegerField(editable=True, blank=True, null=True)
    circuit_id = models.PositiveSmallIntegerField(editable=False)
    circuit_event = models.PositiveSmallIntegerField(editable=False)
    slug = models.ForeignKey(crc_PROG,on_delete=models.CASCADE)
    slug2 = models.SlugField(max_length=10, blank=True, unique=True)
    circuit_mode = models.CharField(max_length=20)
    created = models.DateField(auto_now_add=True, null=True)
    updated = models.DateField(auto_now=True, null=True)
    status1 = models.BooleanField(default=False)
    status2 = models.BooleanField(default=False)
    status3 = models.BooleanField(default=False)
    status4 = models.BooleanField(default=False)
    status5 = models.BooleanField(default=False)
    status6 = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.event_hour}:{self.event_minute} - {self.slug}"
    
    def save(self, *args, **kwargs):
        x = str(self.slug)
        print(x)
        a,b = x.split("-")
        print(a, b)
        self.circuit_id = a
        self.circuit_event = b
        if not self.slug2:
            self.slug2 = '-'.join((slugify(self.event_hour),slugify(self.event_minute),slugify(self.slug)))
        super().save(*args, **kwargs)
