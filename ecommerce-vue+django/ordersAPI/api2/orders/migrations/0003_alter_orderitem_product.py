# Generated by Django 4.0.4 on 2022-04-20 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orderitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.CharField(max_length=100),
        ),
    ]
