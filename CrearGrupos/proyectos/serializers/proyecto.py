from rest_framework import serializers
from proyectos.models import Proyecto

class ProyectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proyecto
        # fields = '__all__'
        fields = ['id','nombre_proyecto', 'descripcion','codigo_fuente']
        # exclude = ["foto"]
