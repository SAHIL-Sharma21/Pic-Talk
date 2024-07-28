from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404, redirect #like ORM which used to talk to database

# Create your views here.
#testing view

def index(request):
    return render(request, 'index.html')


#list all tweets
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})


#create tweets
def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES) #handling form/ making form -> Django superpower
        if form.is_valid():
            tweet = form.save(commit=False) #commit = fasle means db mei store nhi krenge bs form ka data save rahega
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})


#edit tweet / form
def tweet_edit(request):
    pass