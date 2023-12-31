# Generated by Django 4.2.6 on 2023-11-01 05:09

from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_shop_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageShopDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
                ('image1', models.ImageField(blank=True, null=True, upload_to=shop.models.image_detail_path)),
                ('image2', models.ImageField(blank=True, null=True, upload_to=shop.models.image_detail_path)),
                ('image3', models.ImageField(blank=True, null=True, upload_to=shop.models.image_detail_path)),
                ('image4', models.ImageField(blank=True, null=True, upload_to=shop.models.image_detail_path)),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='image_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.imageshopdetail'),
        ),
    ]
