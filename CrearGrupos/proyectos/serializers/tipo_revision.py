from rest_framework import serializers
from proyectos.models import Tipo_Revision

class Tipo_revisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_Revision
        fields = ['id','nombre']

