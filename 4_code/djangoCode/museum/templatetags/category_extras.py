from django import template

register = template.Library()


@register.filter
def first_word(value):
    if not value:
        return ""
    return str(value).strip().split()[0]
