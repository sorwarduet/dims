from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from employees.models import Faculty, Department, UserType, Designation, Employee


class Command(BaseCommand):
    help = 'our help string comes here'

    def _create_designation(self):
        Designation(name='Professor').save()
        Designation(name='Associate Professor').save()
        Designation(name='Assistant Professor').save()
        Designation(name='Lecturer').save()
        Designation(name='System Analyst').save()
        Designation(name='Assistant Programmer').save()
        Designation(name='Assistant Maintenance Engineer').save()
        Designation(name='Junior Maintenance Officer').save()
        Designation(name='Assistant Section Officer').save()
        Designation(name='System Analyst').save()

    def _create_faculty(self):
        pass

    def _create_department(self):
        pass

    def _create_user_type(self):
        pass

    def _create_employee(self):
        pass

    def handle(self, *args, **options):
        self._create_designation()
        self._create_faculty()
        self._create_department()
        self._create_user_type()
        self._create_employee()
