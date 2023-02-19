from django.http.response import HttpResponse
from django.shortcuts import render 
from .models import Categoria
from rest_framework import viewsets
from .serializers import CategoriaSerializer, cellSerializer, prisonerSerializer, guardSerializer
from .models import cells, prisoner, guards
from rest_framework.decorators import api_view
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hola Mundo")

def contact(request,name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")

# def categorias(request):
#     categorias = Categoria.objects.all()
#     return render(request, "categorias.html",{
#         "categorias": categorias
#     })
    
def categorias(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Categoria(nombre= post_nombre)
        q.save()
    
    filtro_nombre = request.GET.get('nombre')
    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre_contains =filtro_nombre)
    else:
        categorias = Categoria.objects.all()
    
    return render( request, "form_categoria.html",{
        "categorias":categorias
    }

    )

class CategoriaViewSet(viewsets.ModelViewSet) :
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class cellsViewSet(viewsets.ModelViewSet) :
    queryset = cells.objects.all()
    serializer_class = cellSerializer

class prisonerViewSet(viewsets.ModelViewSet) :
    queryset = prisoner.objects.all()
    serializer_class = prisonerSerializer

class guardsViewSet(viewsets.ModelViewSet) :
    queryset = guards.objects.all()
    serializer_class = guardSerializer

@api_view(["GET"])
def categoria_count(request):
    """
    Cantidad de items registrados en categoria
    """ 

    try:
        cantidad = Categoria.objects.count()
        return  JsonResponse(
            {
                "cantidad": cantidad
            },
            safe = False,
            status = 200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status= 400)
    
@api_view(["GET"])
def guards_onMorinng(request):
    """
    Cantidad de guardias en la mañana
    """ 

    try:
        morning2 = guards.objects.filter(schedule = 'Mañanas')
        morning = morning2.count()
        return  JsonResponse(
            {
                "cantidad on Morning": morning
            },
            safe = False,
            status = 200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status= 400)