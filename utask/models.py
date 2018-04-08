# -*- coding: utf-8 -*-
from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill


class tasks(models.Model):
    user_name   = models.CharField(u'Имя пользователя', max_length=100)
    user_email  = models.EmailField(u'Email')
    text        = models.TextField(u'Текст задачи')
    #image       = models.ImageField(upload_to='task/', height_field='320', width_field='240')
    image       = ProcessedImageField(
        upload_to='upload',
        processors=[ResizeToFill(320, 240)],
        format='JPEG',
        options={'quality': 100},
        verbose_name=u'Путь до изображения')
    complete    = models.BooleanField(u'Выполнено', default=False)
    datetime_add= models.DateTimeField(u'Дата и время добавления', auto_now_add=True)
    datetime_upd= models.DateTimeField(u'Дата и время обновления', auto_now=True)

    class Meta:
        verbose_name = u'Задача'
        verbose_name_plural = u'Список задач'