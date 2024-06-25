from django.shortcuts import render
from django.http import HttpResponse


def apj(request):
    return HttpResponse("<h1><center>Avul Pakir Jainulabdeen Abdul Kalam<center></h1><h3>Avul Pakir Jainulabdeen Abdul Kalam BR was"
                         " an Indian aerospace scientist and statesman who served as the 11th president of India from" 
                         " 2002 to 2007. Born and raised in a Muslim family in Rameswaram, Tamil Nadu, he studied physics"
                           "and aerospace engineering</h3>")

def sarabhai(request):
    return render(request,'sarabhai.html')