# Generated by Django 3.2.5 on 2022-01-19 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20220119_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='dayDue',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='保质期（单位/月）'),
        ),
    ]
