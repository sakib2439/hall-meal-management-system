# Generated by Django 2.1.2 on 2018-11-15 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0009_auto_20181114_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='user',
        ),
    ]
