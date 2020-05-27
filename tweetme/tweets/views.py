from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

def Home_View(request, *args, **kwargs):
    return HttpResponse("<h1>HelloWOrls</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    ''' REST API VIEW 
        consume by JS, reactnative etc 
        return JSON
    '''
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404

    data = {
        "id": tweet_id,
        "content": obj.content,
    }

    return JsonResponse(data) # json.dumps content_type="application/json"
