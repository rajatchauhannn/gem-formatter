from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from .views import UploadView, process

app_name = 'gem'

urlpatterns = [
    path('', UploadView.as_view(), name='index'),
    path('process/', process, name='process'),
    ]