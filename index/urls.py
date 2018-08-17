from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views, name='index'),
    url(r'^single/(\d+)', single_views),
    url(r'^comment-post/(\d+)', comment_views, name='comment'),
    url(r'^star-post/(\d+)', star_views, name='star'),
    url(r'^addm', addm_views),
    url(r'^addcom', addcom_views),
    url(r'^addstar', addstar_views),
]
