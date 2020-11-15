from django import forms
from .models import Employee, Department, Faculty, WorkRecord, Designation


class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('cell_no', 'address', 'gender', 'dob', 'image', 'employee_no',
                  'joining_date', 'active_status', 'department', 'designation', 'userType')

        widgets = {
            'cell_no': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'dob': DateInput(attrs={'class': 'form-control'}),
            'employee_no': forms.TextInput(attrs={'class': 'form-control'}),
            'joining_date': DateInput(attrs={'class': 'form-control'}),
            'active_status': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
            'userType': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['cell_no'].label = "Cell No"
        self.fields['address'].label = "Address"
        self.fields['gender'].label = "Gender"
        self.fields['dob'].label = "Date of Birth"
        self.fields['employee_no'].label = "Employee No"
        self.fields['joining_date'].label = "Joining Date"
        self.fields['active_status'].label = "Active Status"
        self.fields['department'].label = "Department"
        self.fields['designation'].label = "Designation"
        self.fields['userType'].label = "Employee Type"


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('name', 'code', 'acronym', 'description', 'office_type')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'acronym': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'office_type': forms.Select(attrs={'class': 'form-control'}),
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'code', 'acronym', 'description', 'office_type', 'faculty')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'acronym': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'office_type': forms.Select(attrs={'class': 'form-control'}),
            'faculty': forms.Select(attrs={'class': 'form-control'}),
        }


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ('name', 'description')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
