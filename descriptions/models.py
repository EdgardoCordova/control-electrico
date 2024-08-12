from django.db import models

# Create your models here.
class crc_DES(models.Model):
    circuit_id = models.SmallIntegerField(null=False)
    circuit_description = models.CharField(max_length=100)
    circuit_status = models.BooleanField(null=True)
    date_updated = models.DateField(auto_now=True)
    num_cycles = models.SmallIntegerField(editable=True)
    events_per_cycle = models.SmallIntegerField(editable=True)
    event_duration = models.SmallIntegerField(editable=True)
    random = models.BooleanField(default=False)
    circuit_mode = models.CharField(max_length=20,default="PROG")
    
    def __str__(self):
        return f"{self.circuit_id}"