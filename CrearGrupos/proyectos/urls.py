from django.urls import include, path
from rest_framework import routers


from proyectos.views.rol import *
from proyectos.views.regional import *
from proyectos.views.ficha import *
from proyectos.views.centros_de_formacion import *
from proyectos.views.programa import *
from proyectos.views.perfil import *
from proyectos.views.tipo_revision import *
from proyectos.views.categoria import *
from proyectos.views.proyecto import *
from proyectos.views.equipo_trabajo import *
from proyectos.views.entrega import *
from proyectos.views.documento import *
from proyectos.views.user import *
from proyectos.views.inscrito import InscritoViewSet
from proyectos.views.grupo import GrupoViewSet





router = routers.DefaultRouter()

router.register(r'rol', RolViewSet)
router.register(r'user', UserViewSet)
router.register(r'regional', RegionalViewSet)
router.register(r'ficha', FichaViewSet)
router.register(r'centro', Centros_de_formacionViewSet)
router.register(r'programa', ProgramaViewSet)
router.register(r'perfil', PerfilViewSet)
router.register(r'tipo_revision', Tipo_revisionViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'proyecto', ProyectoViewSet)
router.register(r'equipo_trabajo', Equipo_trabajoViewSet)
router.register(r'entrega', EntregaViewSet)
router.register(r'documento', DocumentoViewSet)
router.register(r'grupo', GrupoViewSet)
router.register(r'inscrito', InscritoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('grupo/<int:pk>/', GrupoDetail.as_view()),
    # path('inscrito/<int:pk>/', InscritoDetail.as_view())

    
]