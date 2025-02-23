"""
URL configuration for westernunion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
#from django.urls import path, include, re_path
from django.urls import include, path
from django.shortcuts import redirect




urlpatterns = [
    path("admin/", admin.site.urls),
    path('', lambda request: redirect('home'), name='redirect_to_home'),
    path("moneytransfer/", include('moneytransfer.urls')),
    #path('', redirect('home'), name='redirect_to_home'),
    #re_path(r'^$', lambda request: redirect('home')),

]
