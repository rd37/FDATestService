'''
Created on Jul 21, 2015

@author: ronaldjosephdesmarais
'''
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',
    # Examples:
    url(r'^submitorder/', views.submitorder, name='order'),

)