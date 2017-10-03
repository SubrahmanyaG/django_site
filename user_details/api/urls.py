from django.conf.urls import include, url
from rest_framework import routers
from user_details.api import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet, 'users')
router.register(r'userDetails', views.UserDetailsViewSet, 'userDetails')

urlpatterns = [
    url(r'^', include(router.urls))
]