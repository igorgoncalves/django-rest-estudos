from rest_framework import serializers
from .models import Cliente, Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'logradouro')

class ClientesSerializer(serializers.ModelSerializer):
    enderecos = EnderecoSerializer(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'enderecos', 'foto')