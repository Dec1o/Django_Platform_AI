import boto3
from django.conf import settings
import os
from dotenv import load_dotenv

class S3Service:
    def __init__(self):
        # Cria uma sessão que automaticamente busca as credenciais na ordem correta
        session = boto3.Session()
        
        # Inicializa o cliente S3 usando a sessão criada
        self.s3 = session.client('s3', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
aws_session_token=os.getenv('AWS_SESSION_TOKEN'))        
        # Define o nome do bucket
        self.bucket_name = settings.BUCKET_NAME

    def upload_file(self, file_obj, file_name):
        """
        Faz upload de um arquivo para o bucket S3.
        :param file_obj: O arquivo a ser enviado
        :param file_name: O nome com o qual o arquivo será armazenado no S3
        """
        
        try:
            print(self.s3.list_buckets())
            self.s3.upload_fileobj(file_obj, self.bucket_name, file_name)
            print(f"Arquivo {file_name} enviado com sucesso!")
            return f"Arquivo {file_name} enviado com sucesso!"
            
        except Exception as e:
            print(f"Erro ao enviar arquivo: {str(e)}")
            return f"Erro ao enviar arquivo: {str(e)}"

    def delete_file(self, file_name):
        """
        Remove um arquivo do bucket S3.
        :param file_name: O nome do arquivo a ser removido
        """
        try:
            self.s3.delete_object(Bucket=self.bucket_name, Key=file_name)
            return f"Arquivo {file_name} removido com sucesso!"
        except Exception as e:
            return f"Erro ao remover arquivo: {str(e)}"

    def get_file_url(self, file_name):
        """
        Gera uma URL de acesso ao arquivo armazenado no S3.
        :param file_name: O nome do arquivo no S3
        :return: URL para acessar o arquivo
        """
        try:
            url = self.s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': file_name},
                ExpiresIn=3600  # URL expira em 1 hora
            )
            return url
        except Exception as e:
            return f"Erro ao gerar URL: {str(e)}"
