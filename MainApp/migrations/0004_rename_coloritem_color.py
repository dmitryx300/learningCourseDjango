# Generated by Django 4.2.3 on 2023-07-13 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_alter_coloritem_name_alter_item_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ColorItem',
            new_name='Color',
        ),
    ]
