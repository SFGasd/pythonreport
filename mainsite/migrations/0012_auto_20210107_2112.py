# Generated by Django 3.1.4 on 2021-01-07 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0011_auto_20210106_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taipeistationinout',
            name='io_amount',
            field=models.CharField(max_length=20),
        ),
    ]
