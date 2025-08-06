from django import template
register = template.Library()

@register.filter
def dict_get(d, key):
    try:
        return d.get(key, 'Low')
    except AttributeError:
        return 'Low'
