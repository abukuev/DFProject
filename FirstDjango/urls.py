"""
URL configuration for FirstDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from MainApp import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.home, name='home_route'),
    path('items', views.get_items, name ='items_route'),
    path('about', views.about, name ='about_route'),
    path('item/<int:itemid>', views.get_item, name ='getitem_route')
]
