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
    url(r'^$', views.index, name = "leaderindex"),
    url(r'^(?P<pk>[0-9]+)/$', views.playerview, name = "playerview"),
    url(r'^dm/(?P<pk>[0-9]+)/$', views.playerdmview, name = "playerdmview"),
    url(r'^recent/$', views.indexrecent, name="leaderindexrecent"),
    url(r'^recent/(?P<pk>[0-9]+)/$', views.playerview, name="playerviewrecent"),
    url(r'^graph/$', views.graph, name = "graphtest"),
    url(r'^dm/$', views.indexdm, name="leaderindexdm"),
    url(r'^dm/recent/$', views.indexdmrecent, name="leaderindexdmrecent"),
    url(r'^dm/recent/(?P<pk>[0-9]+)/$', views.playerdmview, name= "recentplayerdmview"),
]