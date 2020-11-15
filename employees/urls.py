from django.urls import path
from .views import *

urlpatterns = [
    path('employee/', EmployeeListView.as_view(), name='employee_list'),
    path('employee/update/<int:pk>', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/delete/<int:pk>', EmployeeDeleteView.as_view(), name='employee_delete'),

    path('faculty/', FacultyListView.as_view(), name='faculty_list'),
    path('faculty/create', FacultyCreateView.as_view(), name='faculty_create'),
    path('faculty/update/<int:pk>', FacultyUpdateView.as_view(), name='faculty_update'),
    path('faculty/delete/<int:pk>', FacultyDeleteView.as_view(), name='faculty_delete'),

    path('department/', DepartmentListView.as_view(), name='department_list'),
    path('department/create', DepartmentCreateView.as_view(), name='department_create'),
    path('department/update/<int:pk>', DepartmentUpdateView.as_view(), name='department_update'),
    path('department/delete/<int:pk>', DepartmentDeleteView.as_view(), name='department_delete'),

    path('designation/', DesignationListView.as_view(), name='designation_list'),
    path('designation/create', DesignationCreateView.as_view(), name='designation_create'),
    path('designation/update/<int:pk>', DesignationUpdateView.as_view(), name='designation_update'),
    path('designation/delete/<int:pk>', DesignationDeleteView.as_view(), name='designation_delete'),
]
