# Generated by Django 4.0.1 on 2022-02-07 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'favorite',
            },
        ),
    ]
