from django.urls import path
# from .views import api_home
from . import views
urlpatterns = [
    path('', views.api_home)
]
