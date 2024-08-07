# Generated by Django 5.0.7 on 2024-07-14 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_api', '0002_alter_users_create_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('authname', models.CharField(max_length=15)),
                ('auth_time', models.DateTimeField(auto_now=True)),
                ('menus', models.TextField(blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='create_time',
            field=models.IntegerField(default=1720919581.4574847),
        ),
    ]
