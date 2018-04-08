# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('user_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('text', models.TextField(verbose_name='Текст задачи')),
                ('images', imagekit.models.fields.ProcessedImageField(upload_to='static/main_image/teachers', verbose_name='Путь до изображения')),
                ('complete', models.BinaryField(default=False, verbose_name='Выполнено')),
                ('datetime_add', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')),
                ('datetime_upd', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Список задач',
            },
        ),
    ]
