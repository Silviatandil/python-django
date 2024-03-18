from django.urls import path
from .views import Crear_Auto

urlpatterns=[
    path('', Crear_Auto)
]