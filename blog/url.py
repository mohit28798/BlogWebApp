from django.conf import settings
from django.urls import path,re_path,include
from django.conf.urls import url

from blog.views import *


urlpatterns =[
        url(r'^blog/',home,name="home"),
        url(r'^contact/',contact,name='contact'),
        
        url(r'^login/',login,name='login'),
        url(r'^logout/',logout,name='logout'),
        url(r'^loginaccount/',loginaccount,name='loginaccount'),
        url(r'^singleblog/(?P<pk>\d+)/',singleblog,name='singleblog'),
        url(r'^search/',search,name='search'),
        url(r'^subscribe/',subscribe,name='subscribe'),
        url(r'^signup/',signup,name='signup'),
        url(r'^shuffle/',shuffle,name='shuffle'),
        url(r'^createaccount/',createaccount,name='createaccount'),
        url(r'^archive/(?P<pk>\d+)/',archive,name='archive'),
        url(r'^archived/',archived,name='archived'),
        url(r'^feedback/',feedback,name='feedback'),
        url(r'^selectcategory/',selectcategory,name='selectcategory'),
        url(r'^filtered/(?P<pk>\d+)/',filtered,name='filtered'),
        ]

