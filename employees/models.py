from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

# local
from .choices import DEPARTMENT_TYPE, GENDER, ACTIVE_STATUS


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Faculty(TimeStampedModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, blank=True, null=True)
    acronym = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    office_type = models.CharField(max_length=10, choices=DEPARTMENT_TYPE, default='ac')
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Faculty, self).save(*args, **kwargs)


class Department(TimeStampedModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, blank=True, null=True)
    acronym = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    office_type = models.CharField(max_length=10, choices=DEPARTMENT_TYPE, default='ac')
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT, related_name='departments')
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)


class UserType(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(UserType, self).save(*args, **kwargs)


class Designation(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    slug = models.SlugField(editable=False)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Designation, self).save(*args, **kwargs)


class WorkRecord(TimeStampedModel):
    role_name = models.CharField(max_length=100)
    isAdditional = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    assign_date = models.DateField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.role_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.role_name)
        super(WorkRecord, self).save(*args, **kwargs)


class Employee(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee')
    cell_no = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(max_length=300, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='employee/')
    employee_no = models.IntegerField(blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    active_status = models.CharField(max_length=10, choices=ACTIVE_STATUS, default='active')

    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT, related_name='faculty', blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department', blank=True,
                                   null=True)
    userType = models.ForeignKey(UserType, on_delete=models.PROTECT, related_name='userType', blank=True, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT, related_name='designation', blank=True,
                                    null=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Employee, self).save(*args, **kwargs)


def create_user_employee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)


post_save.connect(create_user_employee, sender=settings.AUTH_USER_MODEL)
