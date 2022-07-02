import datetime
from django import template
register=template.Library()
@register.simple_tag(name="get_date")
def get_date():
    x=datetime.datetime.now()
    return x
@register.filter
def quotes(value):
    s='"'+str(value)+'"'
    return s
