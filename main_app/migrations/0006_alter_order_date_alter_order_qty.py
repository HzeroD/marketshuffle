# Generated by Django 4.0 on 2022-01-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
