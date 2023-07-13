# Generated by Django 4.2.3 on 2023-07-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('hex_code', models.CharField(max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='color_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
