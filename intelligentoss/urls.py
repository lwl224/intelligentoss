"""intelligentoss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from smart_import import views

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^set_password/$', views.set_password, name='set_password'),
    url(r'^view_cell/$', views.view_cell, name='view_cell'),
    url(r'^loaddata/$', views.initialization, name='init'),
    url(r'^downdata/$', views.download, name='load'),
    url(r'^upexcel/$', views.upexcel, name='upexcel'),
    url(r'^downmodeexcel/$', views.big_file_download, name='downmodeexcel'),
    url(r'^addcellunion/(.*)/$', views.addcellunion, name='add'),
]
