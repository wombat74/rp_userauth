from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from core.models import Blog

def listing(request):
    data = {
        "blogs": Blog.objects.all(),
    }

    return render(request, "listing.html", data)

def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    data = {
        "blog": blog,
    }

    return render(request, "view_blog.html", data)
