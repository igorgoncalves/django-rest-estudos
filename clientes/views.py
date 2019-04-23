from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Cliente
from .serielizers import ClientesSerializer

# Create your views here.

class ClienteView(APIView):
    
    def get(self, request, id_cliente:int=None):        

        if (id_cliente):
            clientes = Cliente.objects.filter(id=id_cliente)
        else :
            clientes = Cliente.objects.all()            

        if (not clientes):
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = ClientesSerializer(clientes, many=True)

        return Response( { "clientes": serializer.data }, status=status.HTTP_200_OK)
        
    def post(self, request):        

        serializer = ClientesSerializer(data=request.data)        
        
        if serializer.is_valid():            
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        if request.data['id']:

            cliente = Cliente.objects.get(id=request.data['id'])
            serializer = ClientesSerializer(cliente, data=request.data)

            if serializer.is_valid():                        
                serializer.save()             

            return Response(serializer.data, status=status.HTTP_204_NOT_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):

        if request.data['id']:
            cliente = Cliente.objects.get(id=request.data['id'])
            cliente.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    
class EnderecosView(APIView):
    def get(self, request, id_cliente:int=None, id_endereco:int=None):
        return Response( {"enderecos": "none"} )