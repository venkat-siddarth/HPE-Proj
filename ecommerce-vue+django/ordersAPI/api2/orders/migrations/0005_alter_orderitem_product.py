# Generated by Django 4.0.4 on 2022-04-20 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orderitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.IntegerField(default=0),
        ),
    ]
