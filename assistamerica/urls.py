from django.urls import path

from . import views

urlpatterns = [
    path('policy/', views.Policy.as_view({"post": "policy"}), name='policy'),
]
