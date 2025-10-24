from django.urls import path

from .views import (
    Index,
    VentaCreate,
    VentaDelete,
    VentaDetail,
    VentaList,
    VentaUpdate,
)

app_name = "venta"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("venta/", VentaList.as_view(), name="venta_list"),
    path("venta/create/", VentaCreate.as_view(), name="venta_create"),
    path("venta/detail/<int:pk>", VentaDetail.as_view(), name="venta_detail"),
    path("venta/update/<int:pk>", VentaUpdate.as_view(), name="venta_update"),
    path("venta/delete/<int:pk>", VentaDelete.as_view(), name="venta_delete"),
]
