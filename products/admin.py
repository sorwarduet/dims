from django.contrib import admin
from .models import Category, Product, Memo, Status, \
    ProductItem, NonTraceableItem, TraceableItem, Property, Location, \
    ItemAssign, PersonalLoan, PersonalLoanItem, Repair, RepairItem

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Memo)
admin.site.register(Status)
admin.site.register(NonTraceableItem)
admin.site.register(TraceableItem)
admin.site.register(Property)
admin.site.register(Location)
admin.site.register(ItemAssign)
admin.site.register(PersonalLoan)
admin.site.register(PersonalLoanItem)
admin.site.register(Repair)
admin.site.register(RepairItem)
