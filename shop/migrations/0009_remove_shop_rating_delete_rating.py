# Generated by Django 4.2.6 on 2023-12-11 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_sale_percent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='rating',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
