from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from django.conf.urls.static import static
from django.conf import settings
from blog.models import Post
from . import views
urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="blog/blog.html")),

                url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = Post,
                                    template_name="blog/post.html"), name='post_detail'),
                url(r'^post/new/$', views.post_new, name='post_new'),
			]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)