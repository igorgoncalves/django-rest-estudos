from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .mixins import MultipleFieldLookupMixin

from .models import Cliente, Endereco
from .serializers import ClientesSerializer, EnderecoSerializer

# Create your views here.

class ClienteView(ListCreateAPIView):
    serializer_class = ClientesSerializer
    queryset = Cliente.objects.filter(ativo=True)

class ClienteDetailedView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClientesSerializer
    queryset = Cliente.objects.filter(ativo=True)    

class EnderecosView(MultipleFieldLookupMixin, ListCreateAPIView):
    serializer_class = EnderecoSerializer
    queryset = Endereco.objects.all()
    lookup_fields = ['cliente']
    
    def perform_create(self, serializer):
        cliente = Cliente.objects.get(pk=self.kwargs['cliente'])        
        serializer.save(cliente=cliente)

class EnderecosDetailedView(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = EnderecoSerializer
    queryset = Endereco.objects.all()
    lookup_fields = ['cliente', 'pk']