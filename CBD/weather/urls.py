from django.urls import path

from . import views

urlpatterns = [
            path('',views.master),
            path('master',views.master),
            path('index',views.index),
            path('climaDiario',views.climatologiaDiariaList),
            path('estadisticas',views.estadisticas),]