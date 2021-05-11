from django.conf.urls import url 
from django.conf.urls.static import static
from django.conf import settings 
from django.urls import path
from . import views

app_name = 'uploader'

urlpatterns = [
    url(r'^fileupload/$', views.UploadFile, name = 'fileupload'),
    url(r'^filelist/$', views.file_list, name = 'filelist'),
    path('filelist/<int:pk>/', views.DeleteFile, name = 'deletefile'),
]

