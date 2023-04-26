from rest_framework import serializers
from proyectos.models import Perfil
# from django.contrib.auth.models import User 

class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = [ 'id','documento', 'rol', 'usuario']

