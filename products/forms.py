from django import forms
from django.forms.widgets import DateInput
from .models import Category, Product, Location, Memo, Status


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
            'description',
            'parent_id',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country_of_origin': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = (
            'name',
            'description',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = (
            'name',
            'description',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
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
            'tender': forms.TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control'}),
            'received_by': forms.Select(attrs={'class': 'form-control'}),
        }
