from django.urls import path

from ..views.categoria import (
    CategoriaCreate,
    CategoriaDelete,
    CategoriaDetail,
    CategoriaList,
    CategoriaUpdate,
    index,
)

urlpatterns = [
    path("", index, name="index"),
    path("categoria/", CategoriaList.as_view(), name="categoria_list"),
    path("categoria/create/", CategoriaCreate.as_view(), name="categoria_create"),
    path("categoria/detail/<int:pk>", CategoriaDetail.as_view(), name="categoria_detail"),
    path("categoria/update/<int:pk>", CategoriaUpdate.as_view(), name="categoria_update"),
    path("categoria/delete/<int:pk>", CategoriaDelete.as_view(), name="categoria_delete"),
]
