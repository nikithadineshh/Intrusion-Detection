from django.urls import path, re_path
from . import views


urlpatterns = [
    # path('', views.home, name = 'home')
    path('',views.home,name='home'),
    path('',views.result,name='result'),
]