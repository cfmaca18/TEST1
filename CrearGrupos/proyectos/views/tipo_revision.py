from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.tipo_revision import *


class Tipo_revisionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tipo_Revision.objects.all()
    serializer_class = Tipo_revisionSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # get post delete update/put
