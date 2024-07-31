from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name="tweet_list"),
    path('create/', views.create_tweet, name="create_tweet"),
    path('<int:tweet_id>/edit/', views.tweet_edit, name="tweet_edit"),
    path('<int:tweet_id>/delete/', views.tweet_delete, name="tweet_delete"),
    path('register/', views.register, name="register"),
    path('search/', views.search_tweets, name="search_tweets"),
    path('search/<int:tweet_id>/result', views.search_result, name="search_result")
]