from django.urls import path

from ..views.producto import (
    Index,
    ProductoCreate,
    ProductoDelete,
    ProductoDetail,
    ProductoList,
    ProductoUpdate,
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("producto/", ProductoList.as_view(), name="producto_list"),
    path("producto/create/", ProductoCreate.as_view(), name="producto_create"),
    path("producto/detail/<int:pk>", ProductoDetail.as_view(), name="producto_detail"),
    path("producto/update/<int:pk>", ProductoUpdate.as_view(), name="producto_update"),
    path("producto/delete/<int:pk>", ProductoDelete.as_view(), name="producto_delete"),
]
