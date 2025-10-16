import re

from django import forms

from . import models


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        # fields = ["nombre", "descripcion"]
        fields = "__all__"

    def clean_nombre(self):
        # Expresión regular
        patron = r"^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s\-\(\)]+$"

        nombre: str = self.cleaned_data.get("nombre", "")
        nombre = nombre.strip()

        if not re.fullmatch(patron, nombre):
            raise forms.ValidationError(
                "Solo se permiten letras, espacios, paréntesis, acentos,"
                " diéresis y guiones medios. No se admiten números ni caracteres especiales."
            )

        if len(nombre) < 3 or len(nombre) > 50:
            raise forms.ValidationError(
                "Longitud mínima de 3 caracteres y máxima de 50"
            )
        return nombre
