# Generated by Django 4.1.13 on 2024-04-29 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CafeApp', '0004_alter_dish_image_userorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorder',
            name='selected_dishes',
        ),
        migrations.AddField(
            model_name='userorder',
            name='dish',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CafeApp.dish'),
        ),
        migrations.AddField(
            model_name='userorder',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
