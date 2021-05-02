from django.db import models

from bases.models import ClassModel
# Create your models here.

class Cliente(ClassModel):
    NAT='Natural'
    JUR= 'Jurídica'
    TIPO_CLIENTE = [
        (NAT, 'Natural'),
        (JUR, 'Jurídica')
    ]
    nombres = models.CharField(
        max_length=100
    )
    apellidos = models.CharField(
        max_length=100
    )
    direccion=models.CharField(
        max_length=100,
        null=True
    )
    telefono = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    tipo=models.CharField(
        max_length=10,
        choices=TIPO_CLIENTE,
        default=NAT
    )
    email= models.CharField(
        max_length=100,
        unique=True
    )
    identificacion = models.CharField(
        max_length=13,
        unique=True
    )
    

    def __str__(self):
        return'{} {}'.format(self.apellidos,self.nombres)
    
    def save(self):
        self.nombres=self.nombres.upper()
        self.apellidos=self.apellidos.upper()
        self.direccion=self.direccion.upper()
        super(Cliente, self).save()

    class Meta:
        verbose_name_plural = 'Clientes'

