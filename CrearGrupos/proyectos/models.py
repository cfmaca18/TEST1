from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
MODALIDAD = (
    ('presencial', 'Presencial'),
    ('virtual', 'Virtual'),
)

ROL = (
    ('aprendiz', 'Aprendiz'),
    ('instructor', 'Instructor'),
    ('admin', 'Admin'),
    ('anonimo', 'Anonimo'),
)
TIPO_DOCUMENTO = (
    ('CC', 'CC'),
    ('TI', 'TI'),
    ('CE', 'CE'),
    ('PASAPORTE', 'PASAPORTE'),
)

CALIFICACION = (
    ('aprobado', 'Aprobado'),
    ('desaprobado', 'desaprobado'),
)
    
ESTADO_PROYECTO = (
    ('terminado', 'terminado'),
    ('en revision', 'en revision'),
    ('en desarrollo', 'en desarrollo'),
)


class Regional (models.Model):
    nombre          =models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.nombre

class Centros_de_formacion(models.Model):
    nombre          =models.CharField(max_length=300, unique=True)
    direccion       =models.CharField(max_length=100,null= True, blank= True )
    encargado       =models.CharField(max_length=20,null= True, blank= True)
    regional        =models.ForeignKey(Regional, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre + " " + self.regional.nombre
    
class Programa(models.Model):
    nombre               = models.CharField(max_length=300,unique=True)
    centros_de_formacion = models.ForeignKey(Centros_de_formacion, on_delete=models.PROTECT) 
    # Centros de formacion tiene una relacion de UNO a MUCHOS con Programa
       
    def __str__(self):
        return self.nombre


class Ficha(models.Model):

    codigo              = models.PositiveIntegerField(unique=True) 
    fecha_inicio        = models.DateField()
    fecha_finalizacion  = models.DateField()
    modalidad           = models.CharField(max_length=12, choices = MODALIDAD, default='presencial') # Presencial o Virtual
    programa            = models.ForeignKey(Programa, on_delete = models.PROTECT) 
    # Programa tiene una relacion de uno a muchos con Ficha(programa)
    
    def __str__(self):
        return str(self.codigo) + " " + self.programa.nombre

class Rol(models.Model):
    nombre  = models.CharField(max_length=30, choices=ROL, unique=True)
    
    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    documento       = models.PositiveIntegerField(unique=True)
    tipo_documento  = models.CharField(max_length=20, choices = TIPO_DOCUMENTO)
    direccion       = models.CharField(max_length=50,null= True, blank= True)
    telefono        = models.CharField(max_length=15,null= True, blank= True)
    foto            = models.ImageField(upload_to='perfiles', null=True, blank=True)
    web             = models.URLField(null= True, blank= True,)
    rol             = models.ForeignKey(Rol,on_delete = models.PROTECT)
    usuario         = models.OneToOneField(User, on_delete = models.CASCADE)
    creado          = models.DateTimeField(auto_now_add = True)
    editado         = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.usuario.username + " " + self.documento 

class Grupo(models.Model):
    nombre_grupo = models.CharField(max_length=50, unique=True)

    def __str__ (self):
            return self.nombre_grupo
    

class Inscrito(models.Model):
    ESTADO_CHOICES = (

        ('activo', 'Activo'),
        ('inactivo', 'Inactivo')
    )
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    nombre_grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Ficha, on_delete=models.CASCADE)
    proyecto = models.IntegerField()

    def __str__ (self):
        return self.nombre_grupo
        
class Tipo_Revision(models.Model):
    nombre      = models.CharField(max_length=200, unique = True)

    def __str__(self):
        return self.nombre

class Categoria (models.Model):  
    nombre      = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre
    
class Proyecto(models.Model):
    nombre_proyecto     = models.CharField(max_length=300 )    
    descripcion         = models.CharField(max_length=5000 )    
    foto                = models.ImageField(upload_to='proyectos/foto', null=True, blank=True)

    codigo_fuente       = models.URLField(null= True, blank= True,)    
    categorias          = models.ManyToManyField(Categoria, null=True, blank=True)

    # documento       = models.FileField(upload_to = 'proyectos/documentos', null=True, blank=True)  # documento inicial del anteproyecto  
    estado              = models.CharField(max_length=20, choices = ESTADO_PROYECTO, default = 'en revision')
    autor               = models.IntegerField(null= True, blank= True) # consulta el id del usuario que creo la idea usuario que esa conectado 

    creado              = models.DateTimeField(auto_now_add = True)
    editado             = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.nombre_proyecto

    
class Equipo_trabajo (models.Model):
    codigo_grupo    = models.CharField(max_length=15, unique = True) # c+odigo auto generado por medio de un script 
    perfil          = models.ForeignKey(Perfil, on_delete = models.PROTECT) #--- con el correo electronico
    ficha           = models.ForeignKey(Ficha, on_delete = models.PROTECT)
    proyecto        = models.IntegerField(null= True, blank= True) # consulta el id del Proyecto
    
    def __str__(self):
        return self.codigo_grupo


class Entrega (models.Model):
    calificacion            = models.CharField(max_length=20, choices = CALIFICACION,null= True, blank= True)
    descripcion_entrega     = models.CharField(max_length=5000 )    
    respuesta_instructor    = models.CharField(max_length=5000, null= True, blank= True)  
    # Estado_entrega          = models.CharField(max_length=5000 )   
    instructor              = models.CharField(max_length=300 ,null= True, blank= True) # solo va el nombre del instructor que hizo la revision     
    
    proyecto                = models.ForeignKey(Proyecto, on_delete = models.PROTECT )
    tipo_revision           = models.ForeignKey(Tipo_Revision, on_delete = models.PROTECT)
    aprendiz                = models.ForeignKey(Equipo_trabajo, on_delete=models.CASCADE)

    creado                  = models.DateTimeField(auto_now_add = True)
    editado                 = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.calificacion + " " + str(self.creado) + " " + str(self.editado)
    
class Documento (models.Model):
    documento       = models.FileField(upload_to = 'proyectos/documentos',)
    entrega         = models.ForeignKey(Entrega, on_delete=models.CASCADE)
    
    creado          = models.DateTimeField(auto_now_add = True)
    editado         = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.entrega.tipo_revision.nombre