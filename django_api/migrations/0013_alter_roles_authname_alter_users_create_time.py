# Generated by Django 5.0.7 on 2024-07-21 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0012_alter_products_imgs_alter_users_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='authname',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='users',
            name='create_time',
            field=models.IntegerField(default=1721551376.4318755),
        ),
    ]
