from django.shortcuts import render, get_object_or_404
from .models import Post, Attribute
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.utils import timezone
import redis
import inspect

r = redis.StrictRedis(port =6379  ,host ='localhost' ,db = 0)
TODAY = str(timezone.now().date())
 

def home(request):
    r.incr(inspect.currentframe().f_code.co_name +":"+ TODAY)
    return render(request, 'main.html',{} )

def education(request):
    data = Attribute.objects.get(name='Education')
    context = {'selected':'Education','data':data}
    r.incr(inspect.currentframe().f_code.co_name )
    return render(request, 'education.html',context)

def expirience(request):
    data = Attribute.objects.get(name='Expirience')
    context = {'selected':'Expirience','data':data}
    r.incr(inspect.currentframe().f_code.co_name +":"+ TODAY)
    return render(request, 'expirience.html',context)

def about_me(request):
    data = Attribute.objects.get(name='About_me')
    context = {'selected':'About_me','data':data}
    r.incr(inspect.currentframe().f_code.co_name +":"+ TODAY)
    return render(request, 'about_me.html',context)

def back(request):
    data = Attribute.objects.get(name='Back-end')
    context = {'selected':'Back','data':data}
    r.incr(inspect.currentframe().f_code.co_name +":"+ TODAY)
    return render(request, 'back-end.html',context)

def website(request):
    data = Attribute.objects.get(name='Website')
    context = {'selected':'Website','data':data}
    r.incr(inspect.currentframe().f_code.co_name +":"+ TODAY)
    return render(request, 'website.html',context)

def contact(request):
    data = Attribute.objects.get(name='Contact')
    context = {'selected':'Contact','data':data}
    r.incr(inspect.currentframe().f_code.co_name +":"+ TODAY)
    return render(request, 'contact.html',context)

def api_list(request):
    context = {'selected':'Api'}
    r.incr(inspect.currentframe().f_code.co_name +":"+ TODAY)
    return render(request, 'api.html',context)


def post_detail(request, year, month, day, post):
    print(request)
    post = get_object_or_404(Post, slug = post, status = 'published', publish__year = year, publish__month = month, publish__day = day)
    print(post)
    template = 'blog_detail.html'
    context = {'post': post}
    r.incr(inspect.currentframe().f_code.co_name +":"+ TODAY)
    return render(request, template, context)

def skills(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 3) 
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'page': page, 'posts': posts, 'tag':tag,'selected':'Skills'}
    r.incr(inspect.currentframe().f_code.co_name +":"+ TODAY)
    return render(request, 'skills.html', context )