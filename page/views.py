from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from page.models import Page, Post
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect

# Create your views here.
def post(request, page):
    page_id = Page.objects.filter(page_name=page)
    page_name = Post.objects.filter(page=page_id).order_by('order')
    context = {
        'matching_posts': page_name,
    }
    return render(request, 'page/index.html', context)

def edit(request, post, page):

    current_page = page

    if request.method == 'POST':
        this_post = Post.objects.get(id=post)
        this_post.title = request.POST['title']
        this_post.description = request.POST['description']
        this_post.order= request.POST['order']
        this_post.layout= request.POST['layout']
        this_post.save()
        return redirect('/%s/' % (current_page))

def createpost(request, page):

    current_page = Page.objects.get(page_name=page)

    if request.method == 'POST':
        new_title = request.POST['title']
        new_description = request.POST['description']

        try:
            obj = Post.objects.get(page=current_page, title=new_title, description=new_description)
        except Post.DoesNotExist:
            obj = Post(page=current_page, title=new_title, description=new_description)
            obj.save()
        return redirect('/%s/' % (page))