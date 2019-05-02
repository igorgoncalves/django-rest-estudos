from django.contrib import admin

# Register your models here.
from .models import Cliente, Endereco


admin.site.register(Cliente)
admin.site.register(Endereco)