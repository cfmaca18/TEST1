from rest_framework import serializers
from proyectos.models import Inscrito
from proyectos.serializers.grupo import GrupoSerializer
from proyectos.serializers.ficha import FichaSerializer

class InscritoSerializer(serializers.ModelSerializer):
    nombre_grupo = GrupoSerializer()
    perfil = FichaSerializer()

    class Meta:
        model = Inscrito
        fields = ('id', 'estado', 'nombre_grupo', 'perfil', 'proyecto')
    
    def create(self, validated_data):
        nombre_grupo_data = validated_data.pop('nombre_grupo')
        perfil_data = validated_data.pop('perfil')
        
        inscrito = Inscrito.objects.create(**validated_data)

        # Aquí agregamos el código para crear un grupo en caso de que no exista
        nombre_grupo_serializer = GrupoSerializer(data=nombre_grupo_data)
        nombre_grupo_serializer.is_valid(raise_exception=True)
        nombre_grupo = nombre_grupo_serializer.save()

        inscrito.nombre_grupo = nombre_grupo
        inscrito.save()

        FichaSerializer.create(FichaSerializer(), validated_data=perfil_data, inscrito=inscrito)

        return inscrito
