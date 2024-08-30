from django.urls import path
from .views.auth_view import renderRegisterForm,renderLoginForm
from .views.home_view import home,create_blog,blog_detail

urlpatterns  = [
    path('',home,name="home"),
    path('register',renderRegisterForm), 
    path('login',renderLoginForm), 
    path('create',create_blog), 
    path('<int:blog_id>', blog_detail,name='blog_detail')
]