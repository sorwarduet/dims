# Generated by Django 3.0.10 on 2020-09-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
