from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register/', register_views, name='register'),
    url(r'^login/', login_views, name='login'),
]
