# Generated by Django 4.0.4 on 2022-05-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_product_get_absolute_url_product_get_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='_id',
            field=models.IntegerField(default=0),
        ),
    ]
