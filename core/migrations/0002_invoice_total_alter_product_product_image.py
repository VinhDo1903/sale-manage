# Generated by Django 4.0.1 on 2022-02-18 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='default_product.png', upload_to='products_pics'),
        ),
    ]
