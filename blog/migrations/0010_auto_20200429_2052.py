# Generated by Django 3.0.5 on 2020-04-30 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200421_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
