from django import template
from django.template.defaultfilters import floatformat

register = template.Library()

@register.filter(name='custom_format')
def custom_format(value):
    return floatformat(value, 2).replace('.', ',')
