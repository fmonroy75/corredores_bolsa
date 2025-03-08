from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone


class PerfilUsuario(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="perfil"
    )  # Relación uno a uno con User
    saldo = models.IntegerField(
        unique=False, blank=True, null=True,default=100
    )  # Campo adicional
    fecha_registro = models.DateField(
       default=date.today
    )  # Campo adicional

    def __str__(self):
        return f"Perfil de {self.user.username}"
    
class Accion(models.Model):
    simbolo=models.CharField(max_length=30)
    nombre_empresa=models.CharField(max_length=100)
    precio_actual=models.IntegerField(default=0)
    cambio_porcentual=models.IntegerField(default=0)
    fecha_actualizacion=models.DateTimeField(default=timezone.now)  # Campo adicional
        
class Tipo_trx(models.Model):
    id_tipo=models.IntegerField(unique=True, blank=False, null=False,primary_key=True)
    tipotrx =models.CharField(max_length=50) 
    
class Transaccion(models.Model):
    usuario_id=models.ForeignKey(User,on_delete=models.CASCADE)
    accion_id=models.ForeignKey(Accion,on_delete=models.CASCADE)
    tipo_transaccion=models.CharField(max_length=100)
    cantidad=models.IntegerField(default=0)
    Precio =models.IntegerField(default=0)
    tipotrx=models.ForeignKey(Tipo_trx,on_delete=models.CASCADE)
    fecha_transaccion=models.DateTimeField(default=timezone.now)
        
    