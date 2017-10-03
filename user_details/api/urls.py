from django.conf.urls import include, url
from rest_framework import routers
from user_details.api import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet, 'users')

urlpatterns = [
    url(r'^', include(router.urls))
]