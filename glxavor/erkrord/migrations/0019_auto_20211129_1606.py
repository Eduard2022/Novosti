# Generated by Django 3.2 on 2021-11-29 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erkrord', '0018_auto_20211129_1601'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
