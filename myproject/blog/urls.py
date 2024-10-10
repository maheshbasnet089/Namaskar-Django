from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth_view import renderRegisterForm,renderLoginForm
from .views.home_view import blog_list,create_blog,blog_detail,delete_blog,update_blog,profile,edit_profile


urlpatterns  = [
    path('', blog_list, name='blog_list'),
    path('register',renderRegisterForm), 
    path('login/',renderLoginForm), 
    path("logout",auth_views.LogoutView.as_view(),name="logout"),
    path("profile",profile,name='profile'),
    path('<int:blog_id>/delete/', delete_blog, name='delete_blog'),
    path('<int:blog_id>/', blog_detail, name='blog_detail'),
    path('create/', create_blog, name='create_blog'),
    path('<int:blog_id>/edit/', update_blog, name='update_blog'),
    path('profile/edit/', edit_profile, name='edit_profile'),


]