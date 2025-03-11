from rest_framework import serializers
from .models import GroupFile

class GroupFileSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.nome', read_only=True)
    class Meta:
        model = GroupFile
        fields = ['id', 'group_name', 'company','company_name']
    
    def create(self, validated_data):
        # Obtém o ID da empresa e cria o grupo associado
        company_id = validated_data.pop('company')
        group_file = GroupFile.objects.create(company=company_id, **validated_data)
        return group_file
