from rest_framework import serializers

class ConsultaSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=1000)
