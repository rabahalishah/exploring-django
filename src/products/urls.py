"""
URL configuration for trydjango project.

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

from django.urls import path
from .views import dynamic_lookup_view, dynamic_delete_view, product_list_view, product_create_view, product_detail_view

urlpatterns = [
    path('', product_list_view, name='products'),
    path('create/', product_create_view, name='product_create'),
    # path('products/<int:my_id>/', product_detail_view, name='product'),

    # <-- here we are getting id dynamically
    path('<int:my_id>/', dynamic_lookup_view, name='product'),
    # path('products/<int:my_id>/update', product_detail_view, name='product'),
    path('<int:my_id>/delete',
         dynamic_delete_view, name='product-delete'),

]
