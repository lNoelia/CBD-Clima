from django.urls import path

from . import views

urlpatterns = [
            path('climaDiario',views.climatologiaDiariaList),]