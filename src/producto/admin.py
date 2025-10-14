from django.contrib import admin

from . import models


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)


@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("categoria", "nombre", "precio", "stock", "disponible")

    list_display_links = ("nombre",)
    list_filter = ("disponible", "categoria")
    list_editable = ("disponible",)
    search_fields = ("nombre", "descripcion")
