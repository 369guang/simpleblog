from django.shortcuts import render
# Create your views here.
from .models import Post

def post_list(request):
    try:
        posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    except Exception as ex:
        print ex,"-------------------"
    return render(request, 'blog/post_list.html', {'posts':posts})
