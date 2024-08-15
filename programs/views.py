from django.shortcuts import render
from programs.models import crc_PROG
from descriptions.models import crc_DES

def batch_crc_PROG_view(request):
    sum_events = 0
    i = 1
    qs1 = crc_DES.objects.all()
    qs2 = crc_PROG.objects.all()
    if qs2:
        crc_PROG.objects.all().delete()
    a=0
    i=0
    sum_events = 0

    #temp_list[50][6] en python no hay arrays, solo lists, tuples and dictionaries, this is a list
    rows, cols = (50,6)
    temp_list = [[0]*cols]*rows

    for obj in qs1:
        l = 1
        sum_events = sum_events + obj.num_cycles*obj.events_per_cycle
        for j in range(0,obj.num_cycles*obj.events_per_cycle):
            
            id = obj.pk
            print(id)
            
            if id != 0:
                temp_list[i] = [id,l,obj.event_duration,obj.random,obj.circuit_mode]
            
            l = l + 1
            i = i + 1
    
    qs2 = crc_PROG.objects.all()
    print(temp_list)
    
    # save registers in crc_PROG
    for item in temp_list:
        print(item[0],item[1],item[2],item[3],item[4])
        if item[0]>0:
            print(item[0])
            crc_PROG.objects.create(circuit_id_id=item[0], circuit_event=item[1], event_duration=item[2], random=item[3], circuit_mode=item[4])

    context = {
        'qs1': qs1,
        'qs2': qs2,
        'sum_events': sum_events,
    }
    return render(request, 'programs/main.html', context)            