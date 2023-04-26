from rest_framework import serializers
from proyectos.models import Entrega

class EntregaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrega
        fields = ['id','calificacion', 'creado', 'editado']
