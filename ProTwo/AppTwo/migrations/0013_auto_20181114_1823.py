# Generated by Django 2.1.2 on 2018-11-15 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0012_auto_20181114_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal1',
            name='user',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
