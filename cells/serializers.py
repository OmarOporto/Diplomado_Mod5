from rest_framework import serializers
from .models import Categoria, guards, cells, prisoner

class CategoriaSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Categoria
        fields = "__all__"

class cellSerializer(serializers.ModelSerializer) :
    class Meta:
        model = cells
        fields = "__all__"

class prisonerSerializer(serializers.ModelSerializer) :
    class Meta:
        model = prisoner
        fields = "__all__"

class guardSerializer(serializers.ModelSerializer) :
    class Meta:
        model = guards
        fields = "__all__"