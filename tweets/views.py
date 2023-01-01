from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import CreateTweetForm
import random

def home_view(request):
    return render(request, 'tweets/home.html', context=None)


def tweet_list_view(request):
    tweets = Tweet.objects.all().order_by('-id')
    tweet_list = []
    data = {
        'tweet_list': tweet_list
    }
    for tweet in tweets:
        likes = random.randint(0, 100)
        tweet_list.append({'id':tweet.id, 'content': tweet.content, 'likes': likes})
    return JsonResponse(data)


def tweet_detail_view(request, id, *args, **kwargs):
    
    data = {
        'id': id
    }
    status = 200
    try:
        tweet = get_object_or_404(Tweet, pk=id)
        data['content'] = tweet.content
        # return HttpResponse(f'<h1>Tweet ID:{tweet.id} CONTENT:{tweet.content}</h1>')
    except:
        # return HttpResponse('<h2>Tweet {0} not found</h2>'.format(id))
        # or
        # raise Http404
        data['message'] = 'Not found'
        status = 404
    return JsonResponse(data)
    # return HttpResponse(f'Args:{args}, Kwargs:{kwargs}')


def create_tweet_form_view(request):
    form = CreateTweetForm(request.POST or None)
    if form.is_valid():
        return redirect('tweets:home')
    return render(request, 'tweets/create_tweet_form.html', context={'form': form})