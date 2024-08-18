from django.http import HttpResponseRedirect
from django.shortcuts import render


# este programa lo que hace es completar una tabla inicial
def change_theme(request):
    if 'is_dark_mode' in request.session:
        print(request.session['is_dark_mode']) # TOGGLE dark/light MODE
        request.session['is_dark_mode'] = not request.session['is_dark_mode']
    else:
        print(request.session['is_dark_mode']) 
        request.session['is_dark_mode'] = False
    print(request.META.get('HTTP_REFERER'))#tiene la direccion de donde saligo inicialmente
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # este comando regresa a la misma pagina