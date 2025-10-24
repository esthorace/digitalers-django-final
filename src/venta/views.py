from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import VentaForm
from .models import Venta


class Index(TemplateView):
    template_name = "venta/index.html"


class VentaList(ListView):
    model = Venta


class VentaDetail(DetailView):
    model = Venta


class VentaCreate(CreateView):
    model = Venta
    form_class = VentaForm
    success_url = reverse_lazy("venta:venta_list")


class VentaUpdate(UpdateView):
    model = Venta
    form_class = VentaForm
    success_url = reverse_lazy("venta:venta_list")


class VentaDelete(DeleteView):
    model = Venta
    success_url = reverse_lazy("venta:venta_list")
