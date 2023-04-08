from django.db import models
#Esto no nos hace falta para el list
class ClimatologíaDiaria(models.Model):
    fecha= models.DateField(max_length=50,null=False, blank=False)
    indicativo = models.IntegerField(null=False, blank=False)
    nombre = models.CharField(max_length=150,null=False, blank=False)
    provincia = models.CharField(max_length=150,null=False, blank=False)
    altitud = models.FloatField(null=False, blank=False)
    tmed = models.FloatField(null=True, blank=True)
    prec = models.FloatField(null=True, blank=True)
    tmin = models.FloatField(null=True, blank=True)
    horatmin = models.TimeField(null=True, blank=True)
    tmax = models.FloatField(null=True, blank=True)
    horatmax = models.TimeField(null=True, blank=True)
    dir = models.IntegerField(null=True, blank=True)
    velmedia = models.FloatField(null=True, blank=True)
    racha = models.FloatField(null=True, blank=True)
    horaracha = models.CharField(max_length=150,null=True, blank=True)
    sol = models.FloatField(null=True, blank=True)
    presMax = models.FloatField(null=True, blank=True)
    horaPresMax = models.IntegerField(null=True, blank=True)
    presMin = models.FloatField(null=True, blank=True)
    horaPresMin = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.fecha, 
