from django.conf.urls import url 
from . import views

app_name = 'Logging application'

urlpatterns = [
    #main page
    url(r'^$', views.index, name = 'index'),

]
