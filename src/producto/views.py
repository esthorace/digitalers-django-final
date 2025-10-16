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


def categoria_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Categoria.objects.get(id=pk)
    context = {"object": query}
    return render(request, "producto/categoria_detail.html", context)


def categoria_update(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Categoria.objects.get(id=pk)
    if request.method == "GET":
        form = forms.CategoriaForm(instance=query)
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("producto:categoria_list")
    return render(request, "producto/categoria_form.html", {"form": form})


def categoria_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Categoria.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("producto:categoria_list")
    return render(request, "producto/categoria_confirm_delete.html", {"object": query})
