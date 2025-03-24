
from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

# Create your views here.


def blog_page(request, page_num):
    blogs = Blog.published.all()
    paginator = Paginator(blogs, 2)

    try:
        this_page_blogs = paginator.page(page_num)
    except PageNotAnInteger:
        this_page_blogs = paginator.page(1)
    except EmptyPage:
        this_page_blogs = paginator.page(paginator.num_pages)
    except InvalidPage:
        this_page_blogs = paginator.page(1)


    context = {
        "blogs": this_page_blogs,
        "paginator": paginator,
    }

    return render(request, "blog/blog.html", context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status=True)
    return render(request, "blog/blog_detail.html", {"blog": blog})
