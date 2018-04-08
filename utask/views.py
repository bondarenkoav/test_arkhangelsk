# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from imagekit import register, ImageSpec
from pilkit.processors import ResizeToFill
from utask.forms import form_task, LoginForm
from utask.models import tasks
from django.contrib import auth


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


class Thumbnail(ImageSpec):
    processors = [ResizeToFill(100, 50)]
    format = 'JPEG'
    options = {'quality': 60}
register.generator('task:thumbnail', Thumbnail)


def getlist_task(request):      #page_id=1):
    return render(request, 'task_list.html', {'form':form_task,'list_task':tasks.objects.all(),'user':request.user})
    #if page_id==None:
    #        page_id = 1
    #current_page = Paginator(,3)
    #return render(request, 'task_list.html', {'form':form_task,'list_task':current_page.page(page_id),'user':request.user})


def getadd_task(request):
    if request.method == 'POST':
        form = form_task(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task:get_task'))
        else:
            return render(request, 'task_list.html', {'form':form})
    else:
        return HttpResponseRedirect(reverse('task:get_task'))


@login_required
def change_task(request, task_id):
    if request.user.is_superuser:       # Проверим еще разок
        form = form_task(request.POST or None, user=request.user, instance=task_id and tasks.objects.get(id=task_id))
        if request.method == 'POST':
            if form.is_valid():
                old_data = tasks.objects.get(id=task_id)
                new_task = form.save(commit=False)
                new_task.user_name = old_data.user_name
                new_task.user_email = old_data.user_email
                new_task.image = old_data.image
                new_task.save()
                #tasks.objects.filter(id=task_id).update(text=request.POST['text'])
                return HttpResponseRedirect(reverse('task:get_task'))
            else:
                return render(request, 'change_task.html', {'form':form})
        else:
            return render(request, 'change_task.html', {'form':form, 'task_data':tasks.objects.get(id=task_id)})
