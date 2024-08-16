from django.urls import path
from .views import renderRegisterForm,renderLoginForm,renderHomepage

urlpatterns  = [
    path('',renderHomepage),
    path('register',renderRegisterForm), 
    path('login',renderLoginForm)
]