
from django.conf.urls import url
from . import views
from rest_framework import routers
from django.views.generic import RedirectView
# router = routers.DefaultRouter()
# router.register(r'users', views.initClass)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
	# url(r'^/$',RedirectView.as_view(pattern_name='homepage', permanent=True)),
    url(r'list_view', views.ViewBlogList.as_view()),
    url(r'^homepage', views.homepage,name="homepage"),
    url(r'^add-blog', views.add_blog),
    url(r'^view-blog/(?P<blog_id>\d+)/$', views.view_blog),
    url(r'^add_blog_api', views.AddBlog.as_view()),
    url(r'^view_blog_api/(?P<blog_id>\d+)/$', views.ViewBlog.as_view()),
    url(r'^comment_api/(?P<paragraph_id>\d+)/$', views.comment.as_view())
    ]


# path('<int:pk>/', views.DetailView.as_view(), name='detail'),
