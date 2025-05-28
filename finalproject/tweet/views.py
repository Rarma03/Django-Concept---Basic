from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm

# Create your views here.
def index(req):
    return render(req, 'index.html');


# list all the tweet
def AllTweet(req):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(req, 'tweet_list.html', {'tweets': tweets})

# create a tweet
def tweet_create(req):
    if req.method == 'POST':
        form = TweetForm(req.POST, req.FILES)
        # valid hain ya nhi
        if form.is_valid:
            tweet = form.save(commit=False)
            tweet.user = req.user
            tweet.save()
            return redirect('AllTweet')
    else:
        form = TweetForm()

    return render(req, 'tweet_form.html', {'form': form}) 

# editing an existing tweet
def tweet_edit(req, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = req.user)
    if req.method == 'POST':
        form = TweetForm(req.POST, req.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = req.user
            tweet.save()
            return redirect('AllTweet')
    else:
        form = TweetForm(instance=tweet)
    
    return render(req, 'tweet_form.html', {'form': form}) 

# delete the tweet
def tweet_delete(req, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=req.user)
    if req.method == 'POST':
        tweet.delete()
        return redirect('AllTweet')
    
    return render(req, 'tweet_confirm_delete.html', {'tweet':tweet})