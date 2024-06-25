from django.urls import path
from app2.views import *
file_name='anything'

urlpatterns=[
    path('sonunigam/',sonunigam,name='sonunigam'),
    path('kk/',kk,name='kk'),
]