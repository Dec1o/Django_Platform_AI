from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupFileViewSet

router = DefaultRouter()
router.register(r'groups', GroupFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
