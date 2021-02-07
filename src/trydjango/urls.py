"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from pages.views import home_view
from products.views import (
    product_detail_views, product_create_views, render_initial_data, dynamic_lookup_view,
    product_delete_view, product_list_view
)
urlpatterns = [
    path('', home_view, name="home"),
    path('blog/', include('blog.urls')),
    path('product/', product_detail_views, name="prodcut"),
    path('product_create/', product_create_views, name="create"),
    path('render_initial_data/', render_initial_data, name="render_data"),
    path('render_lookup_view/<int:id>/', dynamic_lookup_view, name="product_search"),
    path('product_delete_view/<int:id>/', product_delete_view, name="product_delete_view"),
    path('product_list_all/', product_list_view, name="product_list_all"),
    path('admin/', admin.site.urls),
]
