# Generated by Django 4.1.3 on 2022-11-01 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='secret_key',
        ),
    ]