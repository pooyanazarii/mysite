from django.urls import path
from websit.views import *

app_name = "websit"

urlpatterns = [
    path('',index_view,name='index'),
    path('about',about_view,name='about'),
    path('contact',contact_view,name='contact'),
    path('elements',elements_view,name='elements')
]
