from django.core.management.base import BaseCommand
from employees.models import Faculty, Department, UserType, Designation


class Command(BaseCommand):
    help = 'our help string comes here'

    def _create_designation(self):
        Designation(name='Professor').save()
        Designation(name='Associate Professor').save()
        Designation(name='Assistant Professor').save()
        Designation(name='Lecturer').save()
        Designation(name='System Analyst').save()
        Designation(name='Assistant Maintenance Engineer').save()
        Designation(name='Junior Maintenance Officer').save()
        Designation(name='Assistant Section Officer').save()
        Designation(name='System Analyst').save()

    def handle(self, *args, **options):
        self._create_designation()
