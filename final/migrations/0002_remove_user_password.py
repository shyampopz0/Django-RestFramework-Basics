# Generated by Django 2.2.8 on 2020-09-06 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
