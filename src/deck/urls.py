from django.conf.urls import url
from django.urls import path, include


# /deck/

app_name = 'deck'


from . import views

urlpatterns = [
    
    # url(r'(?P<random_url>[-\w]+)/$', views.index, name='index'),
    url('', views.index, name='index'),


]