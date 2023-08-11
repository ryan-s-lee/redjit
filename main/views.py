from django.shortcuts import render

# Create your views here.

def FeedView(request):
    return render(request, template_name="feed.html")

def ThreadView(request):
    return render(request, "thread.html")