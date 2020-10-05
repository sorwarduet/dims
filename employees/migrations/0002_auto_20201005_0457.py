# Generated by Django 3.0.10 on 2020-10-05 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='designation',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, default='employee/avatar.png', null=True, upload_to='employee/'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='acronym',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='workrecord',
            name='role_name',
            field=models.CharField(max_length=200),
        ),
    ]
