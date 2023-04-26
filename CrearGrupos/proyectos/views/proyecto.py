from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.proyecto import *


class ProyectoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # conocer el usuario que esta conectado en el momento 
    # objeto --- como parametro --- > a una consulta
    
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # get post delete update/put
    
    # def post (self, objeto):
        # consulta para CREAR un PROYECTO (objeto)
        