# Generated by Django 3.0.10 on 2020-10-01 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employees', '0005_auto_20200930_1542'),
        ('products', '0002_auto_20200930_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(editable=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('tender', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(editable=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='memo_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='memo_modified_by', to=settings.AUTH_USER_MODEL)),
                ('received_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='memos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('actual_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('depreciation', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('purchase_date', models.DateField(blank=True, null=True, verbose_name='Purchase Date')),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(editable=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='status_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='status_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='TraceableItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code_key', models.CharField(blank=True, max_length=100, null=True)),
                ('rf_id_key', models.CharField(blank=True, max_length=100, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('warranty_type', models.CharField(choices=[('year', 'Year')], max_length=10)),
                ('warranty_date', models.DateField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='traceableitem_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='traceableitem_modified_by', to=settings.AUTH_USER_MODEL)),
                ('product_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.ProductItem')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Status', verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='property_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='property_modified_by', to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='productitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Category'),
        ),
        migrations.AddField(
            model_name='productitem',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productitem_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productitem',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.Department', verbose_name='Department'),
        ),
        migrations.AddField(
            model_name='productitem',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Location', verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='productitem',
            name='memo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Memo', verbose_name='Memo'),
        ),
        migrations.AddField(
            model_name='productitem',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productitem_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productitem',
            name='parent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_item', to='products.ProductItem'),
        ),
        migrations.AddField(
            model_name='productitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='productitem',
            name='resp_emp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Employee'),
        ),
        migrations.CreateModel(
            name='NonTraceableItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nontraceableitem_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nontraceableitem_modified_by', to=settings.AUTH_USER_MODEL)),
                ('product_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.ProductItem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]