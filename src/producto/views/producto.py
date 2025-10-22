from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from ..forms import ProductoForm
from ..models import Producto


class Index(TemplateView):
    template_name = "producto/index.html"


class ProductoList(ListView):
    model = Producto


class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoDetail(DetailView):
    model = Producto


class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy("producto:producto_list")
