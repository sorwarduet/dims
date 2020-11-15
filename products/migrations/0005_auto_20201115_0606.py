# Generated by Django 3.0.10 on 2020-11-15 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201115_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='product_item_status',
            field=models.CharField(blank=True, choices=[('traceable', 'Traceable'), ('untraceable', 'Untraceable')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]