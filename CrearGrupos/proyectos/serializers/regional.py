from rest_framework import serializers
from proyectos.models import Regional

class RegionalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regional
        fields = [ 'url','id','nombre']



