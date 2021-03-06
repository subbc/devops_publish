"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from . import view
from  HelloWorld.views import (index,login,ansible)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', view.hello),
    url(r'^hellox$', view.hellox),
    url(r'^index$',index.index),
    url(r'^login$',login.login),
    url(r'^register$',login.register),
    url(r'^logout$',login.logout),
    url(r'^baobao$',login.baobao),
    url(r'^a_index$',ansible.index),
    url(r'^publish$',ansible.publish),
]
