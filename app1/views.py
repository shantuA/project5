from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Virat(request):
    return HttpResponse("<h1><center>VIRAT KOHILI<center></h><h3><center>Virat Kohli is an Indian international"
                         "cricketer and the former captain of the Indian national cricket team. He is a right-handed"
                         "batsman and an occasional medium-fast bowler. He currently represents Royal Challengers Bengaluru"
                           "in the IPL and Delhi in domestic cricket.</h3>")

def abd(request):
    return render(request,'abd.html')