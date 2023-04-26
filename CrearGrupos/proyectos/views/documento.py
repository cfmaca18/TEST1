from rest_framework import viewsets
from rest_framework import permissions
from proyectos.serializers.documento import *


class DocumentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # get post delete update/put