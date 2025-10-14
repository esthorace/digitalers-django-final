from django.core.exceptions import ValidationError
from django.db import models


def clean_nombre(nombre: str):
    if nombre:
        nombre = nombre.strip().capitalize()
        if len(nombre) < 3:
            raise ValidationError("El nombre debe tener al menos 3 caracteres.")


class Categoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(verbose_name="descripción", null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Categoría de Producto"
        verbose_name_plural = "Categorías de Productos"

    def clean(self) -> None:
        super().clean()
        clean_nombre(self.nombre)
        return super().clean()


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        related_name="categoria",
        null=True,
        blank=True,
    )
    nombre = models.CharField(max_length=200, db_index=True)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        if self.categoria:
            return f"{self.categoria} - {self.nombre}"
        return self.nombre

    class Meta:
        ordering = ["categoria", "nombre"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def clean(self) -> None:
        super().clean()
        clean_nombre(self.nombre)
        if self.precio < 0:
            raise ValidationError("El precio no puede ser negativo.")
        return super().clean()
