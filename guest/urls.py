"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from sign import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.index),
	url(r'^index/$', views.index),
	url(r'^account/login/$', views.index),
	url(r'^login_action/$', views.login_action),
	url(r'^event_manage/$', views.event_manage),
	url(r'^search_name/$', views.search_name),
	url(r'^guest_manage/$', views.guest_manage),
	url(r'^search_realname/$', views.search_realname),
	url(r'^sign_index/(?P<eid>[0-9]+)/$', views.sign_index),
	url(r'^sign_index_action/(?P<eid>[0-9]+)/$', views.sign_index_action),
	url(r'^logout/$',views.logout),
]