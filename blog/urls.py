
from django.conf.urls import url
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users', views.initClass)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'', views.initClass.as_view()),
]
