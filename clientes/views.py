from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import NotFound

from .models import Cliente, Endereco
from .serializers import ClientesSerializer, EnderecoSerializer

# Create your views here.

class ClienteView(ListCreateAPIView):
    serializer_class = ClientesSerializer
    queryset = Cliente.objects.filter(ativo=True)

    # # def get(self, request, id_cliente:int=None):                        
    #     many=False

    #     if (id_cliente):
    #         try :
    #             clientes = Cliente.objects.get(id=id_cliente, ativo=True)            
    #         except Cliente.DoesNotExist:
    #             raise NotFound("Cliente não encontrado")
    #     else :
    #         clientes = Cliente.objects.filter(ativo=True)
    #         many=True

    #     if (not clientes):
    #         return Response({'detail': 'Nenhum cliente encontrado' }, status=status.HTTP_404_NOT_FOUND)

    #     serializer = ClientesSerializer(clientes, many=many)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

class ClienteDetailedView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClientesSerializer
    queryset = Cliente.objects.filter(ativo=True)
    
    # def post(self, request):        

    #     serializer = ClientesSerializer(data=request.data)        
        
    #     if serializer.is_valid():            
    #         serializer.save() 
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, cliente_id):
        
    #     cliente = Cliente.objects.get(id=cliente_id)
    #     serializer = ClientesSerializer(cliente, data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()

    #     return Response(serializer.data, status=status.HTTP_204_NOT_CONTENT)

    # def delete(self, cliente_id):

        
    #     cliente = Cliente.objects.get(id=cliente_id)
    #     cliente.delete()

    #     return Response(status=status.HTTP_204_NO_CONTENT)

class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj
    
class EnderecosView(MultipleFieldLookupMixin, ListCreateAPIView):
    serializer_class = EnderecoSerializer
    queryset = Endereco.objects.all()
    lookup_fields = ('cliente')

class EnderecosDetailedView(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = EnderecoSerializer
    queryset = Endereco.objects.all()
    lookup_fields = ('pk', 'cliente')