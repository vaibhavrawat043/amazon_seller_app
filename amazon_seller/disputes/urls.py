from django.urls import path
from . import views

urlpatterns = [
    path('', views.dispute_list, name='dispute_list'),
    path('create/', views.create_dispute, name='create_dispute'),
]
