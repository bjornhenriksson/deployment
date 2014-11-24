from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from page.models import Page, Post
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def post(request, page):
    page_id = Page.objects.filter(page_name=page)
    page_name = Post.objects.filter(page=page_id).order_by('order')
    context = {
        'matching_posts': page_name,
    }
    return render(request, 'page/index.html', context)
