from django.conf.urls import url, include
from django.contrib.auth.views import logout
from django.contrib import admin
from sopa.views import *
from sopa import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Login.as_view(), name="login"),
    url(r'^home/', views.home,name='home'),
    url(r'^logout$', logout, name="logout", kwargs={'next_page': '/'}),
    ]
