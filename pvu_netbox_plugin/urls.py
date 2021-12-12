from django.urls import path
from . import views

urlpatterns = [
    path('pontos/', views.PontosView.as_view(), name='pontos'),
]