from django import template

register = template.Library()

@register.inclusion_tag('components/menu_options.html')
def menu_options(menu_items):
    return {'menu_items': menu_items}