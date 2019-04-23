from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = u'Cliente'
        verbose_name_plural = u'Clientes'
        
    def __str__(self):
        return self.nome