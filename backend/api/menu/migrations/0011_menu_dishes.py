# Generated by Django 4.2.1 on 2023-05-21 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_menu_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='dishes',
            field=models.ManyToManyField(related_name='menus', to='menu.dish'),
        ),
    ]