from django.shortcuts import render
from programs.models import crc_PROG
from descriptions.models import crc_DES

def generation_crc_PROG_view(request):
    sum_events = 0
    i = 1
    qs2 = crc_PROG.objects.all()
    qs1 = crc_DES.objects.all()
    
    
    if qs2:
        #pass
        crc_PROG.objects.all().delete()
    
    for instance in qs2:
        pass

    a=0
    i=0
    sum_events = 0
    #temp_list[50][6] en python no hay arrays, solo listas
    rows, cols = (50,6)
    temp_list = [[0]*cols]*rows
    #print(temp_list)

    for obj in qs1:
        l = 1
        sum_events = sum_events + obj.num_cycles*obj.events_per_cycle
        for j in range(0,obj.num_cycles*obj.events_per_cycle):
            #print("crc: ",obj.circuit_id,"event: ",l," / ",obj.num_cycles*obj.events_per_cycle)
            temp_list[i] = [i,obj.circuit_id,l,obj.event_duration,obj.random,obj.circuit_mode]
            l = l + 1
            i = i + 1
    #print(temp_list)
    qs2 = crc_PROG.objects.all()
    #print("qs2:  ... ",qs2)
    #print("suma: ",sum_events)
    
    for item in temp_list:
        x=item[1]
        if (x > 1000):
            if x != 0:
                x=x-1000 # last digit of integer, first converting to string
            print(x,item[2],item[3],item[4],item[5])

            crc_PROG.objects.create(circuit_id_id=x, circuit_event=item[2], event_duration=item[3], random=item[4], circuit_mode=item[5])
        
    
    context = {
        'qs1': qs1,
        'qs2': qs2,
        'sum_events': sum_events,
    }
    return render(request, 'programs/main.html', context)            