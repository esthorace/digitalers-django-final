from django.core.exceptions import ValidationError
from django.db import models


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
        self.nombre = self.nombre.strip()
        self.nombre = f"{self.nombre[0].upper()}{self.nombre[1:]}"
        if len(self.nombre) < 3:
            raise ValidationError(
                "El nombre de la categoría debe tener al menos 3 caracteres."
            )
        return super().clean()
