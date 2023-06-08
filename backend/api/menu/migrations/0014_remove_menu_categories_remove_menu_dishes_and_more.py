# Generated by Django 4.2.1 on 2023-06-08 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_dish_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='dishes',
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='menu.menu'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dish',
            name='menu',
            field=models.ForeignKey(default=14, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='menu.menu'),
            preserve_default=False,
        ),
    ]
