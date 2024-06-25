from django.urls import path
from app3.views import *
file_name='anything'

urlpatterns=[
    path('apj/',apj,name='apj'),
    path('sarabhai/',sarabhai,name='sarabhai'),
]