
from django.conf.urls import url
from . import views
from rest_framework import routers
from django.views.generic import RedirectView
# router = routers.DefaultRouter()
# router.register(r'users', views.initClass)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
	url(r'/',RedirectView.as_view(pattern_name='homepage', permanent=True)),
    url(r'list_view', views.ViewBlogList.as_view()),
    url(r'^homepage', views.homepage,name="homepage"),
    url(r'^add-blog', views.homepage),
    url(r'^view-blog', views.homepage),
]


# path('<int:pk>/', views.DetailView.as_view(), name='detail'),
