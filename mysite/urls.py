from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/logout/', views.logout, name='logout', kwargs={'next_page': 'index'}),
    path('', include('task.urls')),
]
