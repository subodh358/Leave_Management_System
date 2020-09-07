from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Employee, Manager, Staff, Admin
from django.core.exceptions import ValidationError
 
 
class EmployeeSignUpForm(UserCreationForm):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20)
    employee_id = models.PositiveIntegerField(null=False, blank=False)
    my_manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)
    email = models.EmailField(null= False, blank= False)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if Staff.objects.filter(email=email).exists():
            raise ValidationError("email already exists")
        else:
            return email

    def clean_username(self):
        username = self.cleaned_data['username']
        
        if Staff.objects.filter(username=username).exists():
            raise ValidationError("username already exists")
        else:
            return username
    
    def clean_enrollment_number(self):
        employee_id = self.cleaned_data['employee_id']
        
        if Staff.objects.filter(employee_id=employee_id).exists():
            raise ValidationError("employee already exists")
        else:
            return employee_id

    class Meta:
        model = Employee
        fields = UserCreationForm.Meta.fields + ( 'employee_id','first_name', 'last_name', 'email', 'my_manager')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = Employee.EMPLOYEE
        if commit:
            user.save()
        return user



class ManagerSignUpForm(UserCreationForm):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20)
    manager_id = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null= False, blank= False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if Staff.objects.filter(email=email).exists():
            raise ValidationError("email already exists")
        else:
            return email

    def clean_username(self):
        username = self.cleaned_data['username']
        
        if Staff.objects.filter(username=username).exists():
            raise ValidationError("username already exists")
        else:
            return username

    def clean_manager_id(self):
        manager_id = self.cleaned_data['manager_id']
        
        if Manager.objects.filter(manager_id=manager_id).exists():
            raise ValidationError("manager already exists")
        else:
            return manager_id
    

    class Meta:
        model = Manager
        fields = UserCreationForm.Meta.fields + ('manager_id', 'first_name', 'last_name', 'email')
 
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = Manager.MANAGER
        if commit:
            user.save()
        return user


class AdminSignUpForm(UserCreationForm):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20)
    admin_id = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null= False, blank= False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if Staff.objects.filter(email=email).exists():
            raise ValidationError("email already exists")
        else:
            return email

    def clean_username(self):
        username = self.cleaned_data['username']
        
        if Staff.objects.filter(username=username).exists():
            raise ValidationError("username already exists")
        else:
            return username

    def clean_admin_id(self):
        admin_id = self.cleaned_data['admin_id']
        
        if Admin.objects.filter(admin_id=admin_id).exists():
            raise ValidationError("admin already exists")
        else:
            return admin_id
    

    class Meta:
        model = Admin
        fields = UserCreationForm.Meta.fields + ('admin_id', 'first_name', 'last_name', 'email')
 
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = Admin.ADMIN
        if commit:
            user.save()
        return user

