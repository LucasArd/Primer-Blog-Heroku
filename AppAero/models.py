from django.db import models

class Pasajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20) 
    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellido

class Azafatas(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    legajo = models.IntegerField()
    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellido + ' ' + str(self.legajo)


class Piloto(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    horasDeVuelo = models.IntegerField()
    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellido + ' ' + str(self.horasDeVuelo)

class Administrativo(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    legajo = models.IntegerField()
    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellido + ' ' + str(self.legajo)
