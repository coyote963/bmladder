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
from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
import django.contrib.auth.views 
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^login/$', django.contrib.auth.views.login),
    url(r'^logout/$',django.contrib.auth.views.logout), 
    url(r'^blog/',include('blog.urls')),
    url(r'^tinymce/',include('tinymce.urls')),
    url(r'^guides/', include('guides.urls')),
    url(r'^player/',include('player.urls')),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^ladder/',include('ladder.urls')),
    url(r'^clans/',include('clans.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^stats/', include('leaderboards.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^wakemydyno\.txt$',TemplateView.as_view(template_name='wakemydyno.txt')),
    url(r'^djga/', include('google_analytics.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
