# Generated by Django 2.1.2 on 2018-10-29 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181024_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='zh',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
