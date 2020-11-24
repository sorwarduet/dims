from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# local model
from .models import Category, Product, Location, Status, Memo, ProductItem, Property
from .forms import CategoryForm, ProductForm, LocationForm, StatusForm, MemoForm, ProductItemForm, ProductPropertyForm


# Create your views here.

# Category View

class CategoryListView(ListView):
    template_name = 'products/category/category_list.html'
    model = Category
    context_object_name = "categories"


class CategoryCreateView(CreateView):
    template_name = 'products/category/category_add.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    template_name = 'products/category/category_edit.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    template_name = 'products/category/category_delete.html'
    model = Category
    context_object_name = 'category'
    success_url = reverse_lazy('category_list')


# Product view

class ProductListView(ListView):
    template_name = 'products/product/product_list.html'
    model = Product
    context_object_name = "products"


class ProductCreateView(CreateView):
    template_name = 'products/product/product_add.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    template_name = 'products/product/product_edit.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    template_name = 'products/product/product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')

# location View


class LocationListView(ListView):
    template_name = 'products/location/location_list.html'
    model = Location
    context_object_name = "locations"


class LocationCreateView(CreateView):
    template_name = 'products/location/location_add.html'
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy('location_list')


class LocationUpdateView(UpdateView):
    template_name = 'products/location/location_edit.html'
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy('location_list')


class LocationDeleteView(DeleteView):
    template_name = 'products/location/location_delete.html'
    model = Location
    context_object_name = 'location'
    success_url = reverse_lazy('location_list')


# Status View


class StatusListView(ListView):
    template_name = 'products/status/status_list.html'
    model = Status
    context_object_name = "status"


class StatusCreateView(CreateView):
    template_name = 'products/status/status_add.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('status_list')


class StatusUpdateView(UpdateView):
    template_name = 'products/status/status_edit.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('status_list')


class StatusDeleteView(DeleteView):
    template_name = 'products/status/status_delete.html'
    model = Status
    context_object_name = 'status'
    success_url = reverse_lazy('status_list')


# Memo View


class MemoListView(ListView):
    template_name = 'products/memo/memo_list.html'
    model = Memo
    context_object_name = "memos"


class MemoCreateView(CreateView):
    template_name = 'products/memo/memo_add.html'
    model = Memo
    form_class = MemoForm
    success_url = reverse_lazy('memo_list')


class MemoUpdateView(UpdateView):
    template_name = 'products/memo/memo_edit.html'
    model = Memo
    form_class = MemoForm
    success_url = reverse_lazy('memo_list')


class MemoDeleteView(DeleteView):
    template_name = 'products/memo/memo_delete.html'
    model = Memo
    context_object_name = 'memo'
    success_url = reverse_lazy('memo_list')


# product Item view


class ProductItemListView(ListView):
    template_name = 'products/productitem/product_item_list.html'
    model = ProductItem
    context_object_name = "product_items"


class ProductItemCreateView(CreateView):
    template_name = 'products/productitem/product_item_add.html'
    model = ProductItem
    form_class = ProductItemForm
    success_url = reverse_lazy('product_item_list')


class ProductItemUpdateView(UpdateView):
    template_name = 'products/productitem/product_item_edit.html'
    model = ProductItem
    form_class = ProductItemForm
    success_url = reverse_lazy('product_item_list')


class ProductItemDeleteView(DeleteView):
    template_name = 'products/productitem/product_item_delete.html'
    model = ProductItem
    context_object_name = 'product_item'
    success_url = reverse_lazy('product_item_list')

# Property View


class ProductPropertyListView(ListView):
    template_name = 'products/product-property/list.html'
    model = Property
    context_object_name = "properties"


class ProductPropertyCreateView(CreateView):
    template_name = 'products/product-property/add.html'
    model = Property
    form_class = ProductPropertyForm
    success_url = reverse_lazy('product_property_list')


class ProductPropertyUpdateView(UpdateView):
    template_name = 'products/product-property/edit.html'
    model = Property
    form_class = ProductPropertyForm
    success_url = reverse_lazy('product_property_list')


class ProductPropertyDeleteView(DeleteView):
    template_name = 'products/product-property/delete.html'
    model = Property
    context_object_name = 'property'
    success_url = reverse_lazy('product_property_list')
