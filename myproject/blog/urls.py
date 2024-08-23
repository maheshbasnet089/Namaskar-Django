from django.urls import path
from .views.auth_view import renderRegisterForm,renderLoginForm
from .views.home_view import renderHomepage,renderCreateBlogPage

urlpatterns  = [
    path('',renderHomepage),
    path('register',renderRegisterForm), 
    path('login',renderLoginForm), 
    path('create',renderCreateBlogPage)
]