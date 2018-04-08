__author__ = 'ipman'

from django.conf.urls import url
from utask.views import *

urlpatterns = [
    url(r'^change/id-(?P<task_id>\d+)/', change_task, name="change_task"),
    url(r'^add/', getadd_task, name="add_task"),
    #url(r'^(?:page-(?P<page_id>\d+)/)?$', getlist_task, name="get_task"),
    url(r'^$', getlist_task, name="get_task"),
]