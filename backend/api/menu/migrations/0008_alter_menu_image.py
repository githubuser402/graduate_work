# Generated by Django 4.2.1 on 2023-05-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_menu_restaurants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(null=True, upload_to='menu_backgrounds'),
        ),
    ]
