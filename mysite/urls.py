from django.conf.urls import url, include
from django.contrib import admin
from sopa.views import Login
from sopa import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Login.as_view(), name="login"),
    url(r'^home/', views.home,name='home'),
    ]
