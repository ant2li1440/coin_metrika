from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='addpage'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_price, name='post'),
    path('category/<int:cat_id>/', show_category, name='category')
]