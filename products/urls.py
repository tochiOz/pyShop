from django.urls import path
from . import views


# mapping view urls
urlpatterns = [
    path('', views.index),
    path('new', views.new_product)
]