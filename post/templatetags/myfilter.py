# coding=utf-8

from django.template import Library

# 注册我们自定义的标签，只有注册过的标签，系统才能认识你，这是固定写法
register = Library()


@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)
