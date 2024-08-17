from django.db import models

# Create your models here.

MODE_CHOICES = (
    ('#0','ON'),
    ('#1','OFF'),
    ('#2','PROG'),
)

class crc_DES(models.Model):
    circuit_id = models.PositiveSmallIntegerField(null=False)
    circuit_description = models.CharField(max_length=100)
    circuit_status = models.BooleanField(null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    num_cycles = models.PositiveSmallIntegerField(editable=True)
    events_per_cycle = models.PositiveSmallIntegerField(editable=True)
    event_duration = models.PositiveSmallIntegerField(editable=True)
    random = models.BooleanField(default=False)
    circuit_mode = models.CharField(max_length=20,choices=MODE_CHOICES)

    def __str__(self):
        return f"{self.circuit_id}"