from django.urls import re_path,path
from bih.views import *


urlpatterns = [
    re_path(r'^$',HomePage,name='index'),
]

