from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

def catalogo(request):
    productos = Producto.objects.all()
    texto = "Catalogo\n\n"
    for p in productos:
        texto += f"{p.nombre} - "
        texto += f"{p.categoria.nombre} - "

    return HttpResponse(texto,
        content_type="text/plain: charset=utf-8") 

# Create your views here.
