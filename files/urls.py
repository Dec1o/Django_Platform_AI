from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PDFFileViewSet

router = DefaultRouter()
router.register(r'pdfs', PDFFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
