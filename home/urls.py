from django.urls import path
from .views import *


urlpatterns = [
path('', home, name='home'),
path('about', about, name='about'),
path('contact', contact, name='contact'),
path('portfolio', portfolio, name='portfolio'),
path('price', price, name='price'),
path('services', services, name='services'),
path('blog_home', blog_home, name='blog_home'),
path('blog_single', blog_single, name='blog_single'),
]