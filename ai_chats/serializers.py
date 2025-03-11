from rest_framework import serializers
from .models import AIChat

class AIChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIChat
        fields = ['id', 'group', 'chat_name', 'temperature', 'prompt']
