from django import template

register = template.Library()

def nav():
    return {"pages": "hej"}

register.inclusion_tag('page/nav.html')(nav)