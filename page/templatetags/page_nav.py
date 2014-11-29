from django import template
from page.models import Page, Post

register = template.Library()

def nav():
    nav_list = Page.objects.all()
    return {"pages": nav_list}

register.inclusion_tag('page/nav.html')(nav)