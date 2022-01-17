# Generated by Django 3.2.5 on 2022-01-14 12:55

import app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220114_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='create_t',
            field=app.models.TimeStampField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='update_t',
            field=app.models.TimeStampField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_t',
            field=app.models.TimeStampField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_t',
            field=app.models.TimeStampField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
