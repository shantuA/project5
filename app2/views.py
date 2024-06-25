from django.shortcuts import render
from django.http import HttpResponse

def sonunigam(request):
    return HttpResponse("<h1><center>SONU NIGAM<center></h1> <h2>Sonu Nigam is an Indian playback singer,"
                         " music director, dubbing artist and actor. Nigam is a recipient of Padma Shri, India's"
                         " fourth-highest civilian award.</h2>")

def kk(request):
    return render(request,'kk.html')
