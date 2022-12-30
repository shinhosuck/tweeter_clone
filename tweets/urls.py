from django.urls import path
from tweets.views import (
    home_view
)

app_name = 'tweets'


urlpatterns = [
    path('', home_view, name='home'),
]