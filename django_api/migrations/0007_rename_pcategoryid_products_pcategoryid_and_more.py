# Generated by Django 5.0.7 on 2024-07-19 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0006_rename_pcategoryid_products_pcategoryid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='PCategoryId',
            new_name='pCategoryId',
        ),
        migrations.AlterField(
            model_name='users',
            name='create_time',
            field=models.IntegerField(default=1721374526.7532723),
        ),
    ]
