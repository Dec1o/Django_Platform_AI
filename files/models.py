from companies.models import Company
from django.db import models
from django.core.files.storage import default_storage
import os
import uuid

class PDFFile(models.Model):
    def generate_file_path(instance, filename):
        extension = filename.split('.')[-1]
        new_filename = f"{uuid.uuid4()}.{extension}"
        return os.path.join('pdfs/', new_filename)

    file = models.FileField(upload_to=generate_file_path)
    alias = models.CharField(max_length=255)  # Nome original do arquivo
    data_upload = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='pdfs')
    
    # Define 'group' como opcional
    group = models.ForeignKey('groups_files.GroupFile', null=True, blank=True, on_delete=models.CASCADE, related_name='pdfs')

    def __str__(self):
        return os.path.basename(self.file.name)

    def delete(self, *args, **kwargs):
        if self.file:
            file_path = self.file.name  # Caminho no S3
            if default_storage.exists(file_path):
                default_storage.delete(file_path)
        super().delete(*args, **kwargs)

    @property
    def file_name(self):
        return os.path.basename(self.file.name)

    @property
    def file_size(self):
        return round(self.file.size / (1024 * 1024), 2)
