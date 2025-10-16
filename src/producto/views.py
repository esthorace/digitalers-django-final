from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models


def index(request):
    return render(request, "producto/index.html")


# ************** LIST


def categoria_list(request: HttpRequest):
    busqueda = request.GET.get("busqueda")
    if busqueda:
        queryset = models.Categoria.objects.filter(nombre__icontains=busqueda)
    else:
        queryset = models.Categoria.objects.all()
    context = {"object_list": queryset}
    return render(request, "producto/categoria_list.html", context)


class CategoriaList(ListView):
    model = models.Categoria
    # context_object_name = "categorias"
    # template_name = "producto/categoria_lista.html"

    def get_queryset(self) -> QuerySet[Any]:
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = models.Categoria.objects.filter(nombre__icontains=busqueda)
        else:
            queryset = super().get_queryset()
        return queryset


# ************** CREATE


def categoria_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = forms.CategoriaForm()
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:categoria_list")
    return render(request, "producto/categoria_form.html", {"form": form})


class CategoriaCreate(CreateView):
    model = models.Categoria
    form_class = forms.CategoriaForm
    success_url = reverse_lazy("producto:categoria_list")


# ************** DETAIL


def categoria_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Categoria.objects.get(id=pk)
    context = {"object": query}
    return render(request, "producto/categoria_detail.html", context)


class CategoriaDetail(DetailView):
    model = models.Categoria


# ************** UPDATE


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


class CategoriaUpdate(UpdateView):
    model = models.Categoria
    form_class = forms.CategoriaForm
    success_url = reverse_lazy("producto:categoria_list")


# ************** DELETE


def categoria_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = models.Categoria.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("producto:categoria_list")
    return render(request, "producto/categoria_confirm_delete.html", {"object": query})


class CategoriaDelete(DeleteView):
    model = models.Categoria
    success_url = reverse_lazy("producto:categoria_list")
