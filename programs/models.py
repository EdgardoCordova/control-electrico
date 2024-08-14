from django.db import models
from descriptions.models import crc_DES
from django.utils.text import slugify

class crc_PROG(models.Model):
    circuit_id = models.name = models.ForeignKey(crc_DES, on_delete=models.CASCADE)
    circuit_event = models.SmallIntegerField(null=True)
    slug = models.SlugField(max_length=10, blank=True, null=True)
    created = models.DateField(auto_now_add=True, null=True)
    updated = models.DateField(auto_now=True, null=True)
    event_start_hour = models.SmallIntegerField(editable=True, blank=True, null=True)
    event_start_minute = models.SmallIntegerField(editable=True, blank=True, null=True)
    event_duration = models.SmallIntegerField(editable=True, blank=True, null=True)
    random = models.BooleanField(default=False)
    circuit_mode = models.CharField(max_length=20,default="PROG")

    def __str__(self):
        return f"{self.circuit_id} {self.circuit_event}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = '-'.join((slugify(self.circuit_id),slugify(self.circuit_event)))
        super().save(*args, **kwargs)


