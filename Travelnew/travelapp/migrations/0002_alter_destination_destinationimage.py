# Generated by Django 4.1.7 on 2023-03-03 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='destinationImage',
            field=models.ImageField(upload_to='sample'),
        ),
    ]
