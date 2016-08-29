from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings

# Create your views here.
urlpatterns = [
	url(r'^createclan/$', views.clancreate, name='clancreate'),
	url(r'^clan/(?P<slug>\w{1,30})/$', views.clandetail, name='clandetail'),
	url(r'^joinclan/(?P<slug>\w{1,30})/$',views.clanenter, name='clanjoin'),
	url(r'^editclan/(?P<slug>\w+)/$', views.ClanUpdate.as_view(), name='clanupdate'),
	url(r'^$', views.ClanList.as_view(), name="index")
]