# Generated by Django 2.2.13 on 2020-08-31 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20200831_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutorder',
            name='total_amount',
            field=models.IntegerField(verbose_name='Колличество'),
        ),
    ]
