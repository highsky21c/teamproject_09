# Generated by Django 4.0.1 on 2022-02-08 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaveStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.TextField(null=True)),
            ],
            options={
                'db_table': 'stores',
            },
        ),
        migrations.CreateModel(
            name='SaveSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=256)),
                ('stores', models.TextField(null=True)),
            ],
            options={
                'db_table': 'subcategory',
            },
        ),
    ]
