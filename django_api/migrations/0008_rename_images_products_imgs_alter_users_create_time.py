# Generated by Django 5.0.7 on 2024-07-19 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0007_rename_pcategoryid_products_pcategoryid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='images',
            new_name='imgs',
        ),
        migrations.AlterField(
            model_name='users',
            name='create_time',
            field=models.IntegerField(default=1721375309.7394426),
        ),
    ]
