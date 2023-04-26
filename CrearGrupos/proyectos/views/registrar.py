from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from proyectos.serializers.user import *

@api_view(['POST'])
def create_user(request):
        user = User.objects.create(
            username=request.data.get('username'),
            email=request.data.get('email'),
            password=request.data.get('password')
        )
        serializer = UserSerializer(user)