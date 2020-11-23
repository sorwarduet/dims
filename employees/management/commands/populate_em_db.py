from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from employees.models import Faculty, Department, UserType, Designation, Employee
from datetime import  date

class Command(BaseCommand):
    help = 'our help string comes here'

    def _create_designation(self):
        Designation(name='Professor').save()
        Designation(name='Associate Professor').save()
        Designation(name='Assistant Professor').save()
        Designation(name='Lecturer').save()
        Designation(name='Deputy Registrar').save()
        Designation(name='System Analyst').save()
        Designation(name='Assistant Programmer').save()
        Designation(name='Assistant Maintenance Engineer').save()
        Designation(name='Junior Maintenance Officer').save()
        Designation(name='Assistant Section Officer').save()
        Designation(name='System Analyst').save()

    def _create_faculty(self):
        Faculty(name='Civil Engineering').save()
        Faculty(name='Electrical Electronic Engineering').save()
        Faculty(name='Mechanical Engineering').save()
        Faculty(name='science').save()
        Faculty(name='Administrative Offices').save()
        Faculty(name='Office of the Directors').save()

    def _create_department(self):
        faculty_eee = Faculty.objects.get(slug='electrical-electronic-engineering')
        faculty_ce = Faculty.objects.get(slug='civil-engineering')
        faculty_me = Faculty.objects.get(slug='mechanical-engineering')
        faculty_s = Faculty.objects.get(slug='science')
        faculty_ao = Faculty.objects.get(slug='administrative-offices')
        faculty_od = Faculty.objects.get(slug='office-of-the-directors')

        Department(name='Computer Science and Engineering', acronym='CSE',  office_type='ac', faculty=faculty_eee).save()
        Department(name='Electrical Electronics Engineering', acronym='EEE',  office_type='ac', faculty=faculty_eee).save()
        Department(name='Mechanical Engineering', acronym='ME', office_type='ac', faculty=faculty_me,).save()
        Department(name='Civil Engineering', acronym='CE', office_type='ac', faculty=faculty_ce).save()
        Department(name='Textile Engineering', acronym='TE',  office_type='ac',faculty=faculty_me).save()
        Department(name='Industrial Production Engineering', acronym='IPE', office_type='ac', faculty=faculty_me).save()
        Department(name='Architecture', acronym='ARCH', office_type='ac', faculty=faculty_ce).save()
        Department(name='Exam Section', office_type='ad', faculty=faculty_ao).save()
        Department(name='Controller Section', office_type='ad', faculty=faculty_ao).save()
        Department(name='ICT Cell', office_type='ad', faculty=faculty_ao).save()
        Department(name='Transport Section', office_type='ad', faculty=faculty_od).save()

    def _create_user_type(self):
        UserType(name='Teacher').save()
        UserType(name='Officer').save()
        UserType(name='Staff').save()


    def _create_employee(self):
        emp2 = User(username='sorwar', email='sorwar@duet.ac.bd', first_name='Md. Sorwar', last_name='Alam', is_staff=True, is_superuser=True)
        emp2.set_password('1234')
        emp2.save()

        emp1 = User(username='masud', email='masud@duet.ac.bd', first_name='Imran', last_name='Masud', is_staff=True)
        emp1.set_password('1234')
        emp1.save()


    def handle(self, *args, **options):
        #self._create_designation()
        #self._create_faculty()
        #self._create_department()
        #self._create_user_type()
        self._create_employee()
