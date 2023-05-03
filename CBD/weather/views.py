from django.shortcuts import render 
import pymongo
from django.views.decorators.http import require_http_methods
from .forms import *
from django.conf import settings
client = pymongo.MongoClient('mongodb://localhost:27017/')
#Define Db Name
dbname = client['clima']

#Define Collection
climatologiaDiaria = dbname['ClimatologiaDiaria']


climatologiaDiaria_details = climatologiaDiaria.find({}, limit=5)

for r in climatologiaDiaria_details:
    print(r['fecha'])

@require_http_methods("GET")
def master(request):
    return render(request,"master.html", {'STATIC_URL':settings.STATIC_URL})

def index(request):
    return render(request,"index.html", {'STATIC_URL':settings.STATIC_URL})

def climatologiaDiariaList(request):
    piezasLista = climatologiaDiaria.find({}, limit=20)
    search_form = SearchForm()
    if request.method == 'POST':
            search_form = SearchForm(request.POST)
            if search_form.is_valid():
                keyword = search_form.cleaned_data['keyword']
                # piezasLista = climatologiaDiaria.find({'nombre': keyword}, limit=20)
                piezasLista = climatologiaDiaria.find({'nombre': {'$regex':keyword}}, limit=20)
    return render(request,"climaDiario/climatologiaDiaria.html",{'listaClimaDiario' : piezasLista, 'STATIC_URL':settings.STATIC_URL, 'search_form':search_form })

@require_http_methods("GET")
def estadisticas(request):
    piezasLista = climatologiaDiaria.find({}, limit=20)
    context={'listaClimaDiario' : piezasLista , 'STATIC_URL':settings.STATIC_URL}
    return render(request,"climaDiario/estadisticas.html",context)