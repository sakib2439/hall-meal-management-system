# Generated by Django 2.1.2 on 2018-11-15 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0013_auto_20181114_1823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal1',
            old_name='user',
            new_name='username',
        ),
    ]
