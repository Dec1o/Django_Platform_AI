from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('companies.urls')),
    path('api/', include('users.urls')),
    path('api/', include('files.urls')),  
    path('api/', include('groups_files.urls')), 
    path('text_ai/', include('text_ai.urls')),
    path('api/', include('ai_chats.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Configuração para servir arquivos de mídia
