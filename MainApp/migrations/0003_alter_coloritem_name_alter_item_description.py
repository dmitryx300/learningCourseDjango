# Generated by Django 4.2.3 on 2023-07-13 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_coloritem_item_color_id_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coloritem',
            name='name',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default='Базовое описание', max_length=1000),
        ),
    ]