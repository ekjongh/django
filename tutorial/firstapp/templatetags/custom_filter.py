from django import template
register = template.Library()

@register.filter(name='show')
def show(value, args):
    return format(value, args)

@register.filter(name='find_slice')
def find_slice(value, args):
    # if isinstance(value, str):
    #     pass
    # else:
    #     value = str(format(value,','))
    if not isinstance(value, str):
        value = str(format(value,','))
    return value[:args]
