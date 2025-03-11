from django.contrib import admin
from .models import PDFFile

@admin.register(PDFFile)
class PDFFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'data_upload', 'company')  # Corrigido para 'company'
    list_filter = ('company',)  # Corrigido para 'company'
    search_fields = ('file', 'company__name')  # Corrigido para 'company'

    def delete_model(self, request, obj):
        # O arquivo já é deletado no método 'delete' do modelo PDFFile
        super().delete_model(request, obj)
