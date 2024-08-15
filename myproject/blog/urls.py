from django.urls import path
from .views import renderRegisterForm,renderLoginForm

urlpatterns  = [
    path('register',renderRegisterForm), 
    path('login',renderLoginForm)
]