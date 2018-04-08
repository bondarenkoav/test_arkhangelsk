from utask.forms import LoginForm

__author__ = 'ipman'

from django import template

register = template.Library()

@register.inclusion_tag('templatetags/auth.html')
def login_form_tags(user):
    return {'user': user, 'form':LoginForm}