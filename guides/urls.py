"""bmladder URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    url(r'^$',views.guidelist.as_view(),name='guidelist'),
    url(r'^(?P<pk>[0-9]+)/$', views.guidedetail.as_view(), name = 'detail'),
    # url(r'^(?P<guide_id>[\d]+)/edit/$', guideedit, name = 'guideedit'),
    url(r'^create/$',views.guidecreate, name = 'guidecreate'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)