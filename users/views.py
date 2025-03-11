from rest_framework import viewsets, status
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = User.objects.get(email=email)

        if check_password(password, user.password):
            return Response({'message': 'Login bem sucedido'}, status=status.HTTP_200_OK)
        
        else:
            return Response({"error": "Senha incorreta"}, status=status.HTTP_400_BAD_REQUEST)



    except (User.DoesNotExist):
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND) 


