from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.regional import *


class RegionalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Regional.objects.all()
    serializer_class = RegionalSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # get post delete update/put

#     def create(self, validated_data):
#          return Regional.objects.create(validated_data)

#     def update(self, instance, validated_data):
#          instance.codigo = validated_data.get('codigo', instance.codigo)
