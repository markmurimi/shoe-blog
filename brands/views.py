from django.shortcuts import render
from .models import Post,Profile,Brand

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    images = Post.get_posts()
    return render(request, 'home.html', {"images": images})

def search_results(request):
    if 'posts' in request.GET and request.GET["posts"]:
        search_term = request.GET.get("posts")
        searched_posts = Post.search_by_brand_name(search_term)
        message = f"{search_term}"

        return render(request, 'search-results.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search-results.html',{"message":message})

def brandDetails(request, brand_id):
    posts = Post.objects.filter(brand= brand_id).all()
    print(posts)
    return render(request, 'brand-details.html', {"posts": posts})