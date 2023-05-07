from django.urls import path

from . import views

urlpatterns = [
            path('',views.master),
            path('master',views.master),
            path('index',views.index),
            path('climaDiario/',views.climatologiaDiariaList, name="climaDiario"),
            path('estadisticas',views.estadisticas, name="estadisticas"),
            path('detalle/<str:dato_id>', views.detalle, name="detalle"),
            ]