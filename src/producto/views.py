from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from . import forms, models


def index(request):
    return render(request, "producto/index.html")


def categoria_list(request: HttpRequest):
    busqueda = request.GET.get("busqueda")
    if busqueda:
        queryset = models.Categoria.objects.filter(nombre__icontains=busqueda)
    else:
        queryset = models.Categoria.objects.all()
    context = {"object_list": queryset}
    return render(request, "producto/categoria_list.html", context)


def categoria_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = forms.CategoriaForm()
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:categoria_list")
    return render(request, "producto/categoria_form.html", {"form": form})
