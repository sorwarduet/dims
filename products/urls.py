from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/create', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),

    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),

    path('location/', LocationListView.as_view(), name='location_list'),
    path('location/create', LocationCreateView.as_view(), name='location_create'),
    path('location/update/<int:pk>', LocationUpdateView.as_view(), name='location_update'),
    path('location/delete/<int:pk>', LocationDeleteView.as_view(), name='location_delete'),

    path('status/', StatusListView.as_view(), name='status_list'),
    path('status/create', StatusCreateView.as_view(), name='status_create'),
    path('status/update/<int:pk>', StatusUpdateView.as_view(), name='status_update'),
    path('status/delete/<int:pk>', StatusDeleteView.as_view(), name='status_delete'),

    path('memo/', MemoListView.as_view(), name='memo_list'),
    path('memo/create', MemoCreateView.as_view(), name='memo_create'),
    path('memo/update/<int:pk>', MemoUpdateView.as_view(), name='memo_update'),
    path('memo/delete/<int:pk>', MemoDeleteView.as_view(), name='memo_delete'),

    path('productItem/', ProductItemListView.as_view(), name='product_item_list'),
    path('productItem/create', ProductItemCreateView.as_view(), name='product_item_create'),
    path('productItem/update/<int:pk>', ProductItemUpdateView.as_view(), name='product_item_update'),
    path('productItem/delete/<int:pk>', ProductItemDeleteView.as_view(), name='product_item_delete'),

]
