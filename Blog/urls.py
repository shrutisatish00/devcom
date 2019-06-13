from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from Blog.models import Post
from . import views

urlpatterns = [ 
        url (r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:20],template_name="Blog/Blog.html")), 
        url ('create/', views.article_create, name="create"),
        url (r'^(?P<pk>\d+)$', DetailView.as_view(model = Post , template_name = 'Blog/post.html')),
        
        ] 

# Create your views here.
