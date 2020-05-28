from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
import random

def Home_View(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all() #list of django objects
    tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 100)} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    ''' REST API VIEW 
        consume by JS, reactnative etc 
        return JSON
    '''
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404

    

    return JsonResponse(data, status=status) # json.dumps content_type="application/json"
