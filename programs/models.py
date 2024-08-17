from django.db import models
from descriptions.models import crc_DES
from django.utils.text import slugify
from django.urls import reverse

class crc_PROG(models.Model):
    circuit_id = models.name = models.ForeignKey(crc_DES, on_delete=models.CASCADE, related_name='circuits')
    circuit_event = models.PositiveSmallIntegerField(null=True)
    slug = models.SlugField(max_length=10, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    event_start_hour = models.PositiveSmallIntegerField(editable=True, blank=True, null=True)
    event_start_minute = models.PositiveSmallIntegerField(editable=True, blank=True, null=True)
    event_duration = models.PositiveSmallIntegerField(editable=True, blank=True, null=True)
    random = models.BooleanField(default=False)
    circuit_mode = models.CharField(max_length=20,default="PROG")

    # con este property decorator podemos tratar al related name como un campo (field) 
    @property
    def circuits(self):
        return self.circuits.all()
    
    def get_absolute_url(self):
        return reverse("programs:detail", kwargs={"slug": self.slug}) 

    def __str__(self):
        return f"{self.slug}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = '-'.join((slugify(self.circuit_id),slugify(self.circuit_event)))
        super().save(*args, **kwargs)


