from django.urls import path

from .views import ClienteView, ClienteDetailedView, EnderecosView, EnderecosDetailedView

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('clientes/', ClienteView.as_view()),
    path('clientes/<int:pk>', ClienteDetailedView.as_view()),
    path('clientes/<int:cliente>/enderecos/', EnderecosView.as_view()),
    path('clientes/<int:cliente>/enderecos/<int:pk>', EnderecosDetailedView.as_view()),
]