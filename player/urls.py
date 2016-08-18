from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings

# Create your views here.
urlpatterns = [
	#url(r'^player', )
	url(r'^register/$', views.register, name='register'),
	url(r'^user/(?P<user_username>\w{1,30})/$',views.userview, name='userview')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)