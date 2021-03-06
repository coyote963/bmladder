"""ladder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^tournament/(?P<pk>[0-9]+)/$', views.detail.as_view(), name ='detail'),
    url(r'^$', views.index.as_view(), name='ladderindex'), 
    url(r'^tournament/match-history/(?P<pk>[0-9]+)/$',views.matchhistory, name='matchhistory'),
    url(r'^tournament/reportmatch/(?P<pk>[0-9]+)/$', views.reportmatch, name='reportmatch'),
    url(r'^createtournament/$', views.createtournament, name='createtournament'),
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    
]
