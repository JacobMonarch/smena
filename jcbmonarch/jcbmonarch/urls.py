from django.contrib import admin
from django.urls import path, include
from jcbmonarch import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Главная страница
    path('', include('accounts.urls')),  # Авторизация
]