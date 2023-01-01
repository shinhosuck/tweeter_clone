from django.urls import path
from tweets.views import (
    home_view,
    tweet_detail_view,
    tweet_list_view,
    create_tweet_form_view
)

app_name = 'tweets'


urlpatterns = [
    path('', home_view, name='home'),
    path('tweets', tweet_list_view, name='total-tweets'),
    path('detail/<int:id>', tweet_detail_view, name='tweet-detail'),
    path('create/tweet', create_tweet_form_view, name='create-tweet')
]