# Generated by Django 4.0.1 on 2022-02-08 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorite', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='content',
            new_name='store',
        ),
    ]
