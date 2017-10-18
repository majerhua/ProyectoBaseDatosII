from __future__ import unicode_literals


from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from series.models import Serie
from series.serializers import SerieSerializer


from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (

    CreateView,
    UpdateView,
    DeleteView
)

from .models import Proyecto
from .models import ProyectoDocs
from .models import ProyectoCosto





def index(request):
    return render(request, 'series/index.html')

class ProyectoList(ListView):
    model = Proyecto
    template_name = 'series/lista_proyecto.html'


def ProyectoListFunc(request):
    proyectos = Proyecto.objects.filter(vigente='1')
    return render(request,'series/lista_proyecto.html', {'proyectos': proyectos})


class ProyectoCreacion(CreateView):
    model = Proyecto
    success_url = reverse_lazy('list_p')
    fields = ['codigoFase','codigoNivel','codSnip','nombre','fechReg','costoPip','costoDir','codFuncion','codDepartament','codProvincia','codDiestrito','codCli','codEsp','codResp','observacion']
    template_name = 'series/registro_proyecto.html'


class ProyectoUpdate(UpdateView):
    model = Proyecto
    success_url = reverse_lazy('list_p')
    fields = ['codigoFase','codigoNivel','codSnip','nombre','fechReg','costoPip','costoDir','codFuncion','codDepartament','codProvincia','codDiestrito','codCli','codEsp','codResp','observacion']
    template_name='series/update_proyecto.html'


class ProyectoDetail(DetailView):
    model = Proyecto
    template_name='series/detalle_proyecto.html'


class ProyectoDelete(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('list_p')
    template_name='series/delete_proyecto.html'


##ProyetcoDocs

def ProyectoDocsListFunc(request):
    proyectodocs = ProyectoDocs.objects.filter(vigente='1')
    return render(request,'series/lista_proyectodocs.html', {'proyectodocs': proyectodocs})



class ProyectoDocsCreacion(CreateView):
    model = ProyectoDocs
    success_url = reverse_lazy('list_pd')
    fields = ['proyecto','codigoFase','codigoNivel','fechInicio','fechFin','costEst','observacion','estPyto','tipoEntregable','codEntrega','codEsp','codResp']
    template_name = 'series/registro_proyectodocs.html'


class ProyectoDocsUpdate(UpdateView):
    model = ProyectoDocs
    success_url = reverse_lazy('list_pd')
    fields = ['proyecto','codigoFase','codigoNivel','fechInicio','fechFin','costEst','observacion','estPyto','tipoEntregable','codEntrega','codEsp','codResp']
    template_name='series/update_proyectodocs.html'


class ProyectoDocsDetail(DetailView):
    model = ProyectoDocs
    template_name='series/detalle_proyectodocs.html'


class ProyectoDocsDelete(DeleteView):
    model = ProyectoDocs
    success_url = reverse_lazy('list_pd')
    template_name='series/delete_proyectodocs.html'

##Proyecto costo


def ProyectoCostoListFunc(request):
    proyectocostos = ProyectoCosto.objects.filter(vigente='1')
    return render(request,'series/lista_proyectocosto.html', {'proyectocostos': proyectocostos})



class ProyectoCostoCreacion(CreateView):
    model = ProyectoCosto
    success_url = reverse_lazy('list_pc')
    fields = ['proyecto','codigoNivel','costoDir','costoEquipo','costoAdm','costoImp','costoOtros','observacion','costoPIP','codFase']
    template_name = 'series/registro_proyectocosto.html'


class ProyectoCostoUpdate(UpdateView):
    model = ProyectoCosto
    success_url = reverse_lazy('list_pc')
    fields = ['codigoNivel','costoDir','costoEquipo','costoAdm','costoImp','costoOtros','observacion','costoPIP','codFase']
    template_name='series/update_proyectocosto.html'


class ProyectoCostoDetail(DetailView):
    model = ProyectoCosto
    template_name='series/detalle_proyectocosto.html'


class ProyectoCostoDelete(DeleteView):
    model = ProyectoCosto
    success_url = reverse_lazy('list_pc')
    template_name='series/delete_proyectocosto.html'



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def serie_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SerieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def serie_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        serie = Serie.objects.get(pk=pk)
    except Serie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SerieSerializer(serie)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SerieSerializer(serie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        serie.delete()
        return HttpResponse(status=204)