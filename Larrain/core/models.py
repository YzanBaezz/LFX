from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    precio = models.PositiveSmallIntegerField()
    foto = models.ImageField(upload_to="Producto", null= True)
    descripcion = models.TextField(null=True)
    stock = models.PositiveSmallIntegerField(null=True)
    garantia = models.TextField(blank=True,null=True,verbose_name = 'Mas Informacion del Servicio')
    imagen1 = models.ImageField(upload_to="Producto", null= True)
    imagen2 = models.ImageField(upload_to="Producto", null= True)
    imagen3 = models.ImageField(upload_to="Producto", null= True)
    

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'


class Servicio(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    precio = models.PositiveSmallIntegerField()
    foto = models.ImageField(upload_to="Producto", null= True)
    descripcion = models.TextField(null=True)
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'


class Hora(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    numero = models.PositiveBigIntegerField(null=True)
    marca = models.TextField(null=True)
    patente = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    aceptada = models.BooleanField(null=True)
    def __str__(self):
        return f'{self.nombre} -> {self.fecha}'
