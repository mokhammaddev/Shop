# Generated by Django 4.2.6 on 2023-11-01 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_imageshopdetail_shop_image_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='is_sale',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
