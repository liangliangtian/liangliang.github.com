from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^upload/',upload_video,name='upload'),
    url(r'^show', show_image,name='sh'),
    url(r'^dete1/',dete1,name='det'),
    url(r'^result',result,name='res'),
    url(r'^login/', index_login,name='login'),
    url(r'^register/', index_register,name='register'),
    url(r'^logout',index_logout,name='logout'),
    url(r'^reset/$', index_reset,name='reset'),
    url(r'^back/reset/',index_back,name='back'),
    url(r'^',index_views,name='index'),
]