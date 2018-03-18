from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/authorization/', views.authorization, name='authorization'),
    path('accounts/register/', views.register, name='register'),
]