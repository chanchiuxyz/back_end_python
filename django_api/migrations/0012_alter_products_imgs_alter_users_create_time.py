# Generated by Django 5.0.7 on 2024-07-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0011_alter_products_imgs_alter_users_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='imgs',
            field=models.JSONField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='users',
            name='create_time',
            field=models.IntegerField(default=1721376711.8811095),
        ),
    ]
