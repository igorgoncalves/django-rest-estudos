from django.urls import path

from .views import ClienteView, EnderecosView

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('clientes/', ClienteView.as_view()),
    path('clientes/<int:id_cliente>', ClienteView.as_view()),
    path('clientes/<int:id_cliente>/enderecos/', EnderecosView.as_view()),
    path('clientes/<int:id_cliente>/enderecos/<int:id_endereco>', EnderecosView.as_view()),
]