from django.urls import path
from .views import IndexView, consultar

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('consultar/', consultar, name='consultar'),
]
