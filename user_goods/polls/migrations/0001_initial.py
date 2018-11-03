# Generated by Django 2.1.2 on 2018-10-24 11:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zh', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('pub_date', models.DateField(verbose_name=django.utils.timezone.now)),
                ('yue', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
    ]
