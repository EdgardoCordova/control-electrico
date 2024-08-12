from django.shortcuts import render
from .models import crc_DES
import random 

# este programa lo que hace es completar una tabla inicial

def descriptions_generation_view(request):
    # delete table crc_DES
    qs = crc_DES.objects.all()

    if qs:
        crc_DES.objects.all().delete()
    
    crc_DES.objects.create(
        circuit_id=1001, circuit_description="luces camping",circuit_status =True,num_cycles= 1,
        events_per_cycle=1, event_duration=240,random=False,circuit_mode="PROG")
    crc_DES.objects.create(
        circuit_id=1002, circuit_description="ventiladores",circuit_status =True,num_cycles= 3,
        events_per_cycle=2, event_duration=15,random=False,circuit_mode="PROG")
    crc_DES.objects.create(
        circuit_id=1003, circuit_description="motor",circuit_status =False,num_cycles= 1,
        events_per_cycle=1, event_duration=1,random=False,circuit_mode="OFF")
    crc_DES.objects.create(
        circuit_id=1004, circuit_description="riego",circuit_status =True,num_cycles= 1,
        events_per_cycle=2, event_duration=30,random=False,circuit_mode="ON")
    crc_DES.objects.create(
        circuit_id=1005, circuit_description="calentador ",circuit_status =False,num_cycles= 1,
        events_per_cycle=1, event_duration=60,random=False,circuit_mode="OFF")
    crc_DES.objects.create(
        circuit_id=1006, circuit_description="luces emergencia ",circuit_status =True,num_cycles= 2,
        events_per_cycle=3, event_duration=5,random=True,circuit_mode="PROG")
  
    qs = crc_DES.objects.all()
    context = {
        'qs': qs,
    }
    return render(request, 'main.html', context)            

def descriptions_list_view(request):
    qs = crc_DES.objects.all()
    context = {
        'qs': qs,
    }
    return render(request, 'main.html', context)

def descriptions_update_view(request):
    pass