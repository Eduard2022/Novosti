from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import HomeView, ArticleDetailView, contact_us, search_venues, AddCommentView, LikeView, view_profile, \
    ListThreads, CreateThread, ThreadView, CreateMessage

urlpatterns = [
   path('', HomeView.as_view(), name="home"),
   path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
   path('contact-us/', contact_us, name="contact-us"),
   path('search_venues', views.search_venues, name='search-venues'),
   path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
   path('like/<int:pk>', LikeView, name='like_post'),
   path('profile/', view_profile, name='profile'),
   path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),


   path('inbox/', ListThreads.as_view(), name='inbox'),
   path('inbox/create-thread', CreateThread.as_view(), name='create-thread'),
   path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
   path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message')
]
