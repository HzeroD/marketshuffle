# Generated by Django 4.0 on 2022-01-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_volume_stock_market_cap_stock_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='market_cap',
            field=models.CharField(max_length=20),
        ),
    ]
