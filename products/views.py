from django.shortcuts import render
from django.views.generic import ListView

# local model
from .models import Category
# Create your views here.


class CategoryListView(ListView):
    template_name = 'products/category/category_list.html'
    model = Category
    context_object_name = "categories"
