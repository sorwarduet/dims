from django import forms
from .models import Category, Product, Location, Memo, Status, ProductItem


class DateInput(forms.DateInput):
    input_type = 'date'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
            'description',
            'parent_id',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Category Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Enter description'}),
            'parent_id': forms.Select(attrs={'class': 'form-control'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name',
            'country_of_origin',
            'brand',
            'model',
            'description',
            'image',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Name'}),
            'country_of_origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Country Origin'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Model'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Enter Description'}),
        }


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = (
            'name',
            'description',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Enter Description'}),
        }


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = (
            'name',
            'description',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Status'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Enter Description'}),
        }


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = (
            'tender',
            'date',
            'received_by',
        )
        widgets = {
            'tender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Tender Name'}),
            'date': DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Date'}),
            'received_by': forms.Select(attrs={'class': 'form-control'}),
        }


class ProductItemForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        fields = (
            'name',
            'actual_cost',
            'depreciation',
            'purchase_date',
            'department',
            'location',
            'memo',
            'resp_emp',
            'product',
            'parent_id',
            'category',
            'quantity',
            'expiry_date',
            'warranty_type',
            'warranty_date',
            'serial_no',
            'product_item_status',
            'status',
            'description',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Item Name'}),
            'actual_cost': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Actual Cost'}),
            'depreciation': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_date': DateInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'memo': forms.Select(attrs={'class': 'form-control'}),
            'resp_emp': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'parent_id': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Quantity '}),
            'expiry_date': DateInput(attrs={'class': 'form-control'}),
            'warranty_type': forms.Select(attrs={'class': 'form-control'}),
            'warranty_date': DateInput(attrs={'class': 'form-control'}),
            'serial_no': forms.TextInput(attrs={'class': 'form-control'}),
            'product_item_status': forms.Select(attrs={'class': 'form-control',}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '4', 'placeholder': 'Enter Description '}),
        }
