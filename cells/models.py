from django.db import models
from .validators import validar_Castigo
from .validators import sueldo_minimo

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class cells(models.Model):
    number_id = models.IntegerField()
    number_beds = models.IntegerField()
    revision = models.DateTimeField(auto_now_add=True)
    size = models.DecimalField(decimal_places=2, max_digits=10)

    def __int__(self):
        return self.number_id

class prisoner(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    judgment = models.IntegerField()
    id_prisoner = models.IntegerField()
    cell_id = models.ForeignKey(cells, on_delete=models.CASCADE)
    solitary_punishment = models.BooleanField(default=False, validators= [validar_Castigo])
    
class Kitchen(models.Model):
    Menu = models.CharField(max_length = 100)
    Carne = models.IntegerField()
    Numb_Guards_Assigned = models.IntegerField()

Bloque_A = 'BA'
Bloque_B = 'BB'
Bloque_C = 'BC'

bloques = [
    (Bloque_A, 'Bloque A'),
    (Bloque_B, 'Bloque B'),
    (Bloque_C, 'Bloque C'),

]
Horario_A = 'Mañanas'
Horario_B = 'Tardes'
Horario_C = 'Noches'

horarios = [
    (Horario_A, '06:00-14:00'),
    (Horario_B, '14:00-22:00'),
    (Horario_C, '22:00-06:00'),
]

class guards(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    section = models.CharField(max_length = 100,choices=bloques,default = Bloque_A)
    schedule = models.CharField(max_length = 100,choices=horarios,default = Horario_C)
    salary = models.IntegerField(validators=[sueldo_minimo])
    job_title = models.CharField(max_length = 100)