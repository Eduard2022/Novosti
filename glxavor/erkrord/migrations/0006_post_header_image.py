# Generated by Django 3.2 on 2021-11-24 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erkrord', '0005_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]