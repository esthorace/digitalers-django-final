from django import forms

from . import models


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        # fields = ["nombre", "descripcion"]
        fields = "__all__"
