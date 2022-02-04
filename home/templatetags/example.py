from django import template

register = template.Library()


@register.simple_tag()
def is_current(tab_name, path_info):
    from django.urls import resolve
    url_name = resolve(path_info).url_name
    print(tab_name)
    print(url_name)
    if url_name == tab_name:
        return 'current'
    else:
        # print('bye')
        return 'notcurrent'