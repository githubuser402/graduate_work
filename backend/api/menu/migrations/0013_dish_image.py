# Generated by Django 4.2.1 on 2023-06-08 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_remove_menu_restaurants_menu_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.ImageField(default='', upload_to='dish_images'),
            preserve_default=False,
        ),
    ]