from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Serie(models.Model):

    HORROR = 'horror'
    COMEDY = 'comedy'
    ACTION = 'action'
    DRAMA = 'drama'

    CATEGORIES_CHOICES = (
        (HORROR, 'Horror'),
        (COMEDY, 'Comedy'),
        (ACTION, 'Action'),
        (DRAMA, 'Drama'),
    )

    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Distrito(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    codigoFase = models.IntegerField()  
    
    codigoNivel = models.IntegerField()
    codSnip = models.CharField(max_length=10)
    nombre= models.CharField(max_length=100)
    fechReg = models.DateField()    
    costoPip = models.FloatField()  
    costoDir = models.FloatField()
    codFuncion = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    codCli = models.IntegerField()
    codEsp = models.IntegerField()
    codResp = models.IntegerField()
    observacion = models.TextField(max_length=500)
    vigente = models.CharField(max_length=1,default='1')

    def __str__(self):
        return self.nombre

class ProyectoDocs(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    codigoFase = models.IntegerField()  
    codigoNivel = models.IntegerField()
    fechInicio =models.DateField()  
    fechFin = models.DateField()    
    costEst = models.FloatField()
    observacion = models.TextField(max_length=500)
    estPyto = models.IntegerField()
    tipoEntregable = models.IntegerField()
    codEntrega = models.IntegerField()
    codEsp = models.IntegerField()
    codResp = models.IntegerField()
    vigente = models.CharField(max_length=1,default='1')

class ProyectoCosto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    codigoNivel = models.IntegerField()
    costoDir = models.FloatField()
    costoEquipo = models.FloatField()
    costoAdm = models.FloatField()
    costoImp = models.FloatField()
    costoOtros = models.FloatField()
    observacion = models.TextField(max_length=500) 
    costoPIP = models.FloatField()
    vigente = models.CharField(max_length=1,default='1')
    codFase =  models.IntegerField()









