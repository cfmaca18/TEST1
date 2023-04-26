from rest_framework import serializers
from proyectos.models import Documento

class DocumentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Documento
        fields = [ 'id','entrega']
