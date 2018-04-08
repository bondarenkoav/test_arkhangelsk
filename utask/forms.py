# -*- coding: utf-8 -*-
__author__ = 'ipman'

from django.contrib.auth import authenticate
from django import forms
from utask.models import tasks

class form_task(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(form_task, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            if self.user.is_superuser:
                self.fields['user_name'].required = False
                self.fields['user_name'].widget.attrs['disabled'] = 'disabled'
                self.fields['user_email'].required = False
                self.fields['user_email'].widget.attrs['disabled'] = 'disabled'
                self.fields['image'].required = False
                self.fields['image'].widget.attrs['disabled'] = 'disabled'
            else:
                self.fields['user_name'].required = False
                self.fields['user_name'].widget.attrs['disabled'] = 'disabled'
                self.fields['user_email'].required = False
                self.fields['user_email'].widget.attrs['disabled'] = 'disabled'
                self.fields['text'].required = False
                self.fields['text'].widget.attrs['disabled'] = 'disabled'
                self.fields['image'].required = False
                self.fields['image'].widget.attrs['disabled'] = 'disabled'
                self.fields['complete'].required = False
                self.fields['complete'].widget.attrs['disabled'] = 'disabled'
        else:
            self.fields['complete'].required = False
            self.fields['complete'].widget.attrs['disabled'] = 'disabled'

    user_name   = forms.CharField(required=False, label=u'Имя', widget=forms.widgets.TextInput(attrs={'onchange':'migrateDataTask()'}))
    user_email  = forms.EmailField(required=False, label=u'Email', widget=forms.widgets.EmailInput(attrs={'onchange':'migrateDataTask()'}))
    text        = forms.CharField(required=False, label=u'Текст', widget=forms.widgets.Textarea(attrs={'rows':4,'onchange':'migrateDataTask()'}))
    image       = forms.ImageField(required=False, label=u'Изображение', widget=forms.FileInput(attrs={'onchange':'migrateDataTask()'}))

    class Meta:
         model = tasks
         fields = ['user_name', 'user_email', 'text', 'image','complete']


class LoginForm(forms.Form):
    username = forms.CharField(label=u'Логин', widget=forms.TextInput())
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'Имя пользователя и пароль не подходят')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None