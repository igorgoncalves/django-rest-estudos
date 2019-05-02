from django.db import models

# Create your models here.
class Cliente(models.Model):    
    foto = models.ImageField(upload_to="images")
    nome = models.CharField(null=False, max_length=100)
    ativo = models.BooleanField(null=False, default=True)

    def delete (self):
        self.ativo = False
        self.save()

    class Meta:
        verbose_name = u'Cliente'
        verbose_name_plural = u'Clientes'
        
    def __str__(self):
        return self.nome


class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente,  related_name='enderecos', on_delete=models.DO_NOTHING, blank=True)
    logradouro = models.CharField(max_length=200)
    bairro = models.CharField(max_length=120)
    principal = models.BooleanField(default=False)
    
    def save(self):
        if self.principal:
            query = Endereco.objects.filter(principal=True, cliente=self.cliente.id)
            if query.exists:
                for elemento in query:
                    elemento.principal = False
                    elemento.save()
        return super(Endereco, self).save()

