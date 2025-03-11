from rest_framework import viewsets, serializers
from .models import PDFFile
from .serializers import PDFFileSerializer
from .s3_service import S3Service

class PDFFileViewSet(viewsets.ModelViewSet):
    queryset = PDFFile.objects.all()
    serializer_class = PDFFileSerializer
    s3_service = S3Service()  # Instanciando o serviço S3

    def perform_create(self, serializer):
        """
        Faz o upload do arquivo no S3 antes de salvar no banco de dados.
        """
        file_obj = self.request.FILES['file']
        # Gera um nome de arquivo único
        file_name = PDFFile.generate_file_path(None, file_obj.name)  # Chama a função de geração de nome
        
        # Captura o nome original do arquivo
        original_filename = file_obj.name

        try:
            # Faz o upload do arquivo no S3
            print(file_obj)
            upload_response = self.s3_service.upload_file(file_obj, file_name)
        except Exception as e:
            # Loga o erro e lança uma exceção
            self.logger.error(f"Erro ao fazer upload do arquivo: {e}")
            raise serializers.ValidationError("Erro ao fazer upload do arquivo para o S3.")

        # Salva os dados no banco de dados, incluindo o nome original no campo alias
        # Adicionando o 'group' à chamada do serializer
        serializer.save(file=file_name, alias=original_filename)
        return upload_response

    def perform_destroy(self, instance):
        """
        Remove o arquivo do S3 e depois do banco de dados.
        """
        file_name = instance.file.name

        # Remove o arquivo do S3
        delete_response = self.s3_service.delete_file(file_name)

        # Depois remove do banco de dados
        instance.delete()

        return delete_response

    def perform_update(self, serializer):
        """
        Faz o upload do novo arquivo no S3 antes de atualizar os dados no banco de dados.
        """
        # Verifica se um novo arquivo foi enviado
        if 'file' in self.request.FILES:
            file_obj = self.request.FILES['file']
            # Gera um nome de arquivo único
            file_name = PDFFile.generate_file_path(None, file_obj.name)  # Chama a função de geração de nome
            
            original_filename = file_obj.name

            try:
                # Faz o upload do novo arquivo no S3
                upload_response = self.s3_service.upload_file(file_obj, file_name)
            except Exception as e:
                self.logger.error(f"Erro ao fazer upload do arquivo: {e}")
                raise serializers.ValidationError("Erro ao fazer upload do arquivo para o S3.")

            # Salva a atualização no banco de dados, incluindo o novo nome do arquivo
            serializer.save(file=file_name, alias=original_filename)
        else:
            # Se nenhum novo arquivo for enviado, apenas atualiza os outros campos
            serializer.save()
