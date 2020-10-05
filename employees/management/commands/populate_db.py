from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from products.models import Category, Product, Status, Location


class Command(BaseCommand):
    help = 'our help string comes here'

    def _create_category(self):
        pass

    def _create_product(self):
        pass

    def _create_status(self):
        pass
    
    def _create_location(self):
        pass

    def handle(self, *args, **options):
        self._create_category()
        self._create_product()
        self._create_status()
        self._create_location()

