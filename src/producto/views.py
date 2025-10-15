from django.shortcuts import render

from . import models


def index(request):
    return render(request, "producto/index.html")


def categoria_list(request):
    queryset = models.Categoria.objects.all()
    context = {"object_list": queryset}
    return render(request, "producto/categoria_list.html", context)
