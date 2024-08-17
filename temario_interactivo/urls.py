from django.contrib import admin
from django.urls import path
from temario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('generar_pdf/', views.generar_pdf, name='generar_pdf'),
]
