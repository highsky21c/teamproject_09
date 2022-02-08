# Generated by Django 4.0.1 on 2022-02-08 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('phone_num', models.CharField(max_length=45)),
                ('last_order', models.CharField(max_length=45)),
                ('web_link', models.CharField(max_length=150)),
                ('operating_time', models.CharField(max_length=150)),
                ('break_time', models.CharField(max_length=45)),
                ('holiday', models.CharField(max_length=45)),
                ('pic', models.CharField(max_length=500)),
                ('menu', models.CharField(max_length=200)),
                ('kind_of_food', models.CharField(max_length=100)),
                ('price_range', models.CharField(max_length=45)),
                ('parking', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Store',
            },
        ),
    ]
