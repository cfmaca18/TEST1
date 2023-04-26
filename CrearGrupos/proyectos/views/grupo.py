from rest_framework import viewsets
from proyectos.models import Grupo
from proyectos.serializers.grupo import GrupoSerializer


class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

# class GrupoDetail(viewsets.ModelViewSet):
#     queryset = Grupo.objects.all()
#     serializer_class = GrupoSerializer

