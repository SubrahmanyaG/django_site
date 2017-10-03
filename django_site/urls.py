from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include

from user_details.views import get_index_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index_page, name='index'),
    url(r'^api/', include('user_details.api.urls'))
]
