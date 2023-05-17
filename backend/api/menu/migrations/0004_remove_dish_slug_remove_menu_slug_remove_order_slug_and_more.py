# Generated by Django 4.2.1 on 2023-05-16 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_rename_link_table_slug_order_slug_restaurant_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='order',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='table',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
        migrations.AlterField(
            model_name='ingradient',
            name='slug',
            field=models.SlugField(max_length=60),
        ),
    ]