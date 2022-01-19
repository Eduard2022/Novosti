# Generated by Django 3.2 on 2021-11-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erkrord', '0017_auto_20211128_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
