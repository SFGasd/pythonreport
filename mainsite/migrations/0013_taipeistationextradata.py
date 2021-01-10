# Generated by Django 3.1.4 on 2021-01-10 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0012_auto_20210107_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaipeiStationExtraData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_date', models.CharField(max_length=10)),
                ('total_mileage', models.CharField(max_length=10)),
                ('total_persontimes', models.CharField(max_length=20)),
                ('total_income', models.CharField(max_length=20)),
            ],
        ),
    ]
