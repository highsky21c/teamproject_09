# Generated by Django 4.0.2 on 2022-02-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'subcategory',
            },
        ),
    ]
