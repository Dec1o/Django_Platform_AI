from rest_framework import serializers
from .models import PDFFile

class PDFFileSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(source='company.nome', read_only=True)
    group_name = serializers.CharField(source='group.group_name', read_only=True)
    data_upload = serializers.SerializerMethodField()

    class Meta:
        model = PDFFile
        fields = ['id', 'file', 'data_upload', 'company', 'alias', 'group', 'company_name', 'group_name']  
        read_only_fields = ['alias']

    def create(self, validated_data):
        group_id = validated_data.pop('group', None)  # O parâmetro 'group' é opcional
        company_id = validated_data.pop('company')  # Obter o ID da empresa

        # Cria a instância do PDFFile
        pdf_file = PDFFile.objects.create(company=company_id, group=group_id, **validated_data)
        return pdf_file
    
    def get_data_upload(self, obj):
        return obj.data_upload.strftime('%d/%m/%Y %H:%M')
