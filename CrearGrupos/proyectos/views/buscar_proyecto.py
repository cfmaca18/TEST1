from django.db.models import Q
from rest_framework import generics
from proyectos.models import Proyecto
from proyectos.serializers.proyecto import *

class ProyectoList(generics.ListAPIView):
    serializer_class = ProyectoSerializer

    def get_queryset(self):
        queryset = Proyecto.objects.all()
        search_value = self.request.query_params.get('search', None)
        # cat = Categoria.objects.get(nombre = search_value) # None ERROR  get_or_404  
        
        if search_value is not None:
            queryset = queryset.filter(Q(nombre_proyecto__icontains=search_value) | Q(descripcion__icontains=search_value))
        return queryset
