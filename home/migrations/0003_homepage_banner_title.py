# Generated by Django 4.2.6 on 2023-10-26 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(default='Welcome to my homepage', max_length=100),
        ),
    ]
