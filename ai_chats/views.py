from rest_framework import viewsets
from .models import AIChat
from .serializers import AIChatSerializer

class AIChatViewSet(viewsets.ModelViewSet):
    queryset = AIChat.objects.all()
    serializer_class = AIChatSerializer
  