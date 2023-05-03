from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter(name='modulo')
def modulo(num, val):
    return num % val


@register.filter(name='plus')
def plus(num):
    return num + 1

@register.filter
def intdot(value):
    return intcomma(value).replace(",", ".")