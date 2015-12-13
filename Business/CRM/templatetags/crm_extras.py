from django import template
from django.template.defaulttags import register

register = template.Library()

@register.filter
def to_class_name(value):
    return value.__class__.__name__

@register.filter
def get_item(dictionary, key):
        return dictionary.get(key)
