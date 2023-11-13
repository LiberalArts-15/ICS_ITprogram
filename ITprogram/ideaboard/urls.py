from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView, LogoutView
from . import views

urlpatterns = [
    #login/out#
    path('', views.IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    #まだ開発中ページ#
    path('<str:main_menu>', views.idea_detail),
    
    #post#
    path(
        'posts/<int:post_id>/', 
        views.PostDetailView.as_view(),
        name="view_detail"),
        
    path('posts/new/', views.PostCreateView.as_view(), name="post-create"),

    path(
        'posts/<int:post_id>/edit/', 
        views.PostUpdateView.as_view(), 
        name="post-update"),
    
    path(
        'posts/<int:post_id>/delete/', 
        views.PostDeleteView.as_view(), 
        name="post-delete"),

    #profile#
    path("users/<int:user_id>/", views.ProfileView.as_view(), name="profile"),

    path("edit-profile/", views.ProfileUpdateView.as_view(), name="profile-update"),
]
