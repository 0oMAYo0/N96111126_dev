# Generated by Django 4.1 on 2022-08-17 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
