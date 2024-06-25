from django.urls import path
from app1.views import *
file_name='anything'

urlpatterns = [
    path('Virat/',Virat,name='Virat'),
    path('abd/',abd,name='abd'),

]