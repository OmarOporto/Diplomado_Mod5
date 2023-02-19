from django.core.exceptions import ValidationError


def validar_Castigo(value):
    if value:
        raise ValidationError(
            'el prisionero debe estar en confinamiento solitario'
        )
    
def sueldo_minimo(value):
    v = 2200
    if value < v:
        raise ValidationError('el sueldo minimo es de 2200 bs')
