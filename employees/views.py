from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from .forms import *

from django.contrib.auth.models import User
from .models import *

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


# Employee

class EmployeeListView(LoginRequiredMixin, ListView):
    template_name = 'employee/employee/employee_list.html'
    model = Employee
    context_object_name = "employees"


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'employee/employee/employee_edit.html'
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_list')


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'employee/employee/employee_delete.html'
    model = Employee
    context_object_name = 'employee'
    success_url = reverse_lazy('employee_list')


# Faculty

class FacultyListView(LoginRequiredMixin, ListView):
    template_name = 'employee/faculty/faculty_list.html'
    model = Faculty
    context_object_name = "faculties"


class FacultyCreateView(LoginRequiredMixin, CreateView):
    template_name = 'employee/faculty/faculty_add.html'
    model = Faculty
    form_class = FacultyForm
    success_url = reverse_lazy('faculty_list')


class FacultyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'employee/faculty/faculty_edit.html'
    model = Faculty
    form_class = FacultyForm
    success_url = reverse_lazy('faculty_list')


class FacultyDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'employee/faculty/faculty_delete.html'
    model = Faculty
    context_object_name = 'faculty'
    success_url = reverse_lazy('faculty_list')


# Department

class DepartmentListView(LoginRequiredMixin, ListView):
    template_name = 'employee/department/department_list.html'
    model = Department
    context_object_name = "departments"


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'employee/department/department_add.html'
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department_list')


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'employee/department/department_edit.html'
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department_list')


class DepartmentDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'employee/department/department_delete.html'
    model = Department
    context_object_name = 'department'
    success_url = reverse_lazy('department_list')


# Designation

class DesignationListView(LoginRequiredMixin, ListView):
    template_name = 'employee/designation/designation_list.html'
    model = Designation
    context_object_name = "designations"


class DesignationCreateView(LoginRequiredMixin, CreateView):
    template_name = 'employee/designation/designation_add.html'
    model = Designation
    form_class = DesignationForm
    success_url = reverse_lazy('designation_list')


class DesignationUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'employee/designation/designation_edit.html'
    model = Designation
    form_class = DesignationForm
    success_url = reverse_lazy('designation_list')


class DesignationDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'employee/designation/designation_delete.html'
    model = Designation
    context_object_name = 'designation'
    success_url = reverse_lazy('designation_list')
