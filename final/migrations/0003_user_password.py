# Generated by Django 2.2.8 on 2020-09-07 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0002_remove_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
    ]
