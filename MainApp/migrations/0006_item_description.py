# Generated by Django 5.0.6 on 2024-06-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_remove_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Описание элемента', max_length=900),
        ),
    ]