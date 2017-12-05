
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include
from django.views.static import serve
from apps.base.api.login_logout_authentication import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/bs/', include('apps.base.urls')),
    url(r'^static/(?P<path>.*)$',serve, {}),
    url(r'^api/login/$', login),
]
