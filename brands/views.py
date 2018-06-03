from django.shortcuts import render
from .models import Post,Profile,Brand

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    images = Post.get_posts()
    return render(request, 'home.html', {"images": images})