from django.shortcuts import render 
from django.http import HttpResponse
import pymongo
from django.views.decorators.http import require_http_methods
from .models import ClimatologíaDiaria
from django.conf import settings
client = pymongo.MongoClient('mongodb://localhost:27017/')
#Define Db Name
dbname = client['clima']

#Define Collection
climatologiaDiaria = dbname['climatologiasDiarias']


climatologiaDiaria_details = climatologiaDiaria.find({})

for r in climatologiaDiaria_details:
    print(r['fecha'])

@require_http_methods("GET")
def master(request):
    return render(request,"master.html", {'STATIC_URL':settings.STATIC_URL})

def index(request):
    return render(request,"index.html", {'STATIC_URL':settings.STATIC_URL})

@require_http_methods("GET")
def climatologiaDiariaList(request):
    piezasLista = climatologiaDiaria.find({})
    context={'listaClimaDiario' : piezasLista, 'STATIC_URL':settings.STATIC_URL }
    return render(request,"climaDiario/climatologiaDiaria.html",context)

@require_http_methods("GET")
def estadisticas(request):
    piezasLista = climatologiaDiaria.find({})
    context={'listaClimaDiario' : piezasLista , 'STATIC_URL':settings.STATIC_URL}
    return render(request,"climaDiario/estadisticas.html",context)