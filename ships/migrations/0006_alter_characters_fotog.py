# Generated by Django 4.1.1 on 2022-09-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0005_characters_fotog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='fotog',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
