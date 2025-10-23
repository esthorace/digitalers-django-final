from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserCreationForm, ProfileForm


def index(request):
    return render(request, "core/index.html")


class RegisterCreate(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("core:login")


class ProfileUpdate(UpdateView):
    model = get_user_model()  # Obtiene el modelo User que se puede cambiar en settings
    form_class = ProfileForm
    success_url = reverse_lazy("core:index")

    def get_object(self):
        # UpdateView está esperando un PK: este método hace que devuelva el usuario actual
        # y no se levante un error
        return self.request.user
