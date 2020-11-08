from django.db import models
from django.conf import settings

from django.template.defaultfilters import slugify
# local
from .choices import ACTIVE_STATUS, TYPE, ASSIGNED_RETURNED_STATUS

# local apps
from employees.models import Department

# Create your models here.

""""
Below this model create for Product

"""


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=ACTIVE_STATUS, default='active')
    parent_id = models.ForeignKey('self', blank=True, null=True, related_name='category', on_delete=models.SET_NULL)

    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Product(TimeStampedModel):
    name = models.CharField(max_length=200)
    country_of_origin = models.CharField(max_length=200, blank=True, null=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', default='products/image.png', null=True, blank=True)  # default="employee_images/product_pic.png"

    slug = models.SlugField(editable=False)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Status(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Status, self).save(*args, **kwargs)


class Location(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Location, self).save(*args, **kwargs)


class Memo(TimeStampedModel):
    tender = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    received_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True,  related_name="memos")
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.tender

    def save(self, *args, **kwargs):
        self.slug = slugify(self.tender)
        super(Memo, self).save(*args, **kwargs)


class ProductItem(TimeStampedModel):
    name = models.CharField(max_length=200)
    actual_cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    depreciation = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    purchase_date = models.DateField(verbose_name='Purchase Date', blank=True, null=True)
    department = models.ForeignKey(Department, verbose_name='Department', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, verbose_name='Location', on_delete=models.CASCADE)
    memo = models.ForeignKey(Memo, verbose_name='Memo', on_delete=models.CASCADE)
    resp_emp = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Employee', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, unique=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    quantity = models.DecimalField(max_digits=15, decimal_places=2)

    qr_code_key = models.CharField(max_length=200, blank=True, null=True)
    rf_id_key = models.CharField(max_length=200, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)

    # create type beforehand. check employee/models -> employee -> gender
    warranty_type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True )
    warranty_date = models.DateField(blank=True, null=True)
    status = models.ForeignKey(Status, verbose_name='Status', on_delete=models.DO_NOTHING, null=True, blank=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductItem, self).save(*args, **kwargs)


class Property(TimeStampedModel):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)

    # I think this foreign key should be from ProductItem Table. Also please study on_delete attribute
    product_id = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)


    def __str__(self):
        return self.name


""""
 Below this model for Assign 
"""


class ItemAssign(TimeStampedModel):
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    assigned_employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    assigned_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    assigned_quantity = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    assigned_returned_status = models.CharField(max_length=10, choices=ASSIGNED_RETURNED_STATUS)
    assigned_location = models.ForeignKey(Location, verbose_name='Assigned Location', on_delete=models.CASCADE)


    def __str__(self):
        return self.assigned_employee.username


""""
 Below this model for Loan 
"""


class PersonalLoan(TimeStampedModel):
    loan_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    to_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.to_id.username


class PersonalLoanItem(TimeStampedModel):
    loan_pay_off_time = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    personalLoan = models.ForeignKey(PersonalLoan, on_delete=models.CASCADE)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=ASSIGNED_RETURNED_STATUS)

    def __str__(self):
        return self.product_item.name



""""
 Below this model for Repair  
"""


class Repair(TimeStampedModel):
    repair_request_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    res_employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.repair_request_date


class RepairItem(TimeStampedModel):
    delivery_date = models.DateField()
    actual_cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    estimated_cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=ASSIGNED_RETURNED_STATUS)
    repair_location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.delivery_date


