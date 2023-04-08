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
def climatologiaDiariaList(request):
    piezasLista = climatologiaDiaria.find({})
    context={'listaClimaDiario' : piezasLista }
    return render(request=request,template_name="climaDiario/climatologiaDiaria.html",context=context)