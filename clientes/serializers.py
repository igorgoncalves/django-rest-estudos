from rest_framework import serializers
from .models import Cliente, Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'logradouro', 'principal', 'cliente')
    
    def create (self, validated_data):        
        novo_endereco = Endereco(**validated_data)
        novo_endereco.save()
        return novo_endereco
         

class ClientesSerializer(serializers.ModelSerializer):
    enderecos = EnderecoSerializer(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'enderecos', 'foto')
