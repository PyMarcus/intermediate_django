# Generated by Django 4.1.7 on 2023-03-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create at'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modify',
            field=models.DateTimeField(auto_now=True, verbose_name='Update at'),
        ),
    ]