from rest_framework import serializers
from proyectos.models import Categoria

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']
