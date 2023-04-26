from rest_framework import serializers
from proyectos.models import Equipo_trabajo

class Equipo_trabajoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipo_trabajo
        fields = [ 'id','codigo_grupo']
