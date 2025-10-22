from .urls_patterns import categoria, producto

app_name = "producto"

urlpatterns = [
    *categoria.urlpatterns,
    *producto.urlpatterns,
]
