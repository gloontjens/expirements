'''
Created on Oct 21, 2016

@author: Glenn
'''

from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^$', views.post_list, name='post_list'),
    
]