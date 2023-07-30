from django.urls import path,include, reverse_lazy
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('', views.index, name='home'),
    path('index', views.index, name='home'),

    # Базовые для авторизации
    path('accounts/', include('django.contrib.auth.urls')),

    path('lusher_results/', views.lusher_recieve_result, name='lusher_results'),
    # path('get/', views.get_interpretation_result, name='get_interpretation_result'),
    path('get_interpretation_result/', views.get_interpretation_result, name='get_interpretation_result'),

 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)