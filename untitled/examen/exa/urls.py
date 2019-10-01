from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.urls import path, re_path

from . import views

app_name = 'exa'


urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/', views.user_list, name="user_list"),
    ]
