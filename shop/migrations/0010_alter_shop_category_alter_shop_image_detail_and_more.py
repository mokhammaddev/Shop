# Generated by Django 4.2.6 on 2023-12-11 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_shop_rating_delete_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='image_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.imageshopdetail'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.size'),
        ),
    ]
