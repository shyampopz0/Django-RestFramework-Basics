# Generated by Django 2.2.8 on 2020-09-06 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200905_2357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraccountget',
            options={},
        ),
        migrations.AlterModelManagers(
            name='useraccountget',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='useraccountget',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='useraccountget',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='useraccountget',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='useraccountget',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='useraccountget',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='useraccountget',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='useraccountget',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='useraccountget',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='useraccountget',
            name='password',
        ),
        migrations.RemoveField(
            model_name='useraccountget',
            name='user_permissions',
        ),
    ]
