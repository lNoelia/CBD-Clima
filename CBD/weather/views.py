from bson import ObjectId
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 
import pymongo
from django.views.decorators.http import require_http_methods
from .forms import *
from django.conf import settings
client = pymongo.MongoClient('mongodb://localhost:27017/')
#Define Db Name
dbname = client['clima']

#Define Collection
climatologiaDiaria = dbname['climatologiaDiaria']
estadisticasDatos = dbname['estadisticas']


@require_http_methods("GET")
def master(request):
    return render(request,"master.html", {'STATIC_URL':settings.STATIC_URL})

def index(request):
    return render(request,"index.html", {'STATIC_URL':settings.STATIC_URL})

def climatologiaDiariaList(request):
    piezasLista = climatologiaDiaria.find({}, limit=20)
    lista=[]
    for p in climatologiaDiaria.find({}, limit=20):
        lista.append(str(p['_id']))
    listadas = zip(piezasLista, lista)
    search_form = SearchForm()
    if request.method == 'POST':
            lista=[]
            search_form = SearchForm(request.POST)
            if search_form.is_valid():
                keyword = search_form.cleaned_data['keyword']
                piezasLista = climatologiaDiaria.find({ '$or': [{'nombre': {'$regex':keyword, '$options':'i'}},
                                                       {'provincia': {'$regex':keyword, '$options':'i'}}]}, limit=20)
                for p in climatologiaDiaria.find({ '$or': [{'nombre': {'$regex':keyword, '$options':'i'}},
                                                       {'provincia': {'$regex':keyword, '$options':'i'}}]}, limit=20):
                    lista.append(p['_id'])
                listadas = zip(piezasLista, lista)
    return render(request,"climaDiario/climatologiaDiaria.html",{'STATIC_URL':settings.STATIC_URL, 
                    'search_form':search_form, 'listadas':listadas })

def detalle(request, dato_id):
    pieza = climatologiaDiaria.find_one({'_id': ObjectId(dato_id)})
    return render(request,"climaDiario/detalle.html",{'STATIC_URL':settings.STATIC_URL, 'pieza':pieza })


def estadisticas(request):
    estadisticas = estadisticasDatos.find({}, limit=20)
    lista=[]
    for e in estadisticasDatos.find({}, limit=20):
        lista.append(e['_id'])
    listadas = zip(estadisticas, lista)
    context={'listadas' : listadas , 'STATIC_URL':settings.STATIC_URL}
    return render(request,"climaDiario/estadisticas.html",context)