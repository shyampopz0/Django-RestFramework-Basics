# Generated by Django 2.2.8 on 2020-09-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraccount_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccountGet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]
