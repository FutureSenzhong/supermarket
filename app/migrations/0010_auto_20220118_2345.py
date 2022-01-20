# Generated by Django 3.2.5 on 2022-01-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20220118_2314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '商品列表', 'verbose_name_plural': '商品列表'},
        ),
        migrations.AlterModelOptions(
            name='goodscategory',
            options={'verbose_name': '商品分类', 'verbose_name_plural': '商品分类'},
        ),
        migrations.AddField(
            model_name='goods',
            name='number',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='库存'),
        ),
    ]
