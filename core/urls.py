from django.urls import path, include
from .views import *

urlpatterns = [
    path('about/', about),
    path('contact/', contact),
    path('furnitures/', furnitures),
    path('index/', index),
    path('testimonial/', testimonial),
]
