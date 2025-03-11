from rest_framework import viewsets, serializers
from .models import GroupFile
from .serializers import GroupFileSerializer
from files.models import PDFFile
from files.serializers import PDFFileSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class GroupFileViewSet(viewsets.ModelViewSet):
    queryset = GroupFile.objects.all()
    serializer_class = GroupFileSerializer

    @action(detail=True, methods=['get'])
    def pdfs(self, request, pk=None):
        pdfs = PDFFile.objects.filter(group_id=pk)
        serializer = PDFFileSerializer(pdfs, many=True)
        return Response(serializer.data)

    def perform_destroy(self, instance):
        """
        Impede a exclusão de um grupo se houver arquivos PDF associados.
        """
        if instance.pdfs.exists():  # Verifica se há arquivos associados
            raise serializers.ValidationError("Não é possível excluir o grupo porque existem arquivos associados.")
        
        super().perform_destroy(instance)
