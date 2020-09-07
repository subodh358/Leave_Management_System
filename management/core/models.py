from django.db import models
from django.contrib.auth.models import AbstractUser
 

class Staff(AbstractUser):
    EMPLOYEE = 1
    MANAGER = 2
    ADMIN = 3
    ROLE_CHOICES = (
          (EMPLOYEE, 'Employee'),
          (MANAGER, 'Manager'),
          (ADMIN, 'ADMIN')
    )
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(null= False, blank= False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=False, null=False)

class Manager(Staff):
    manager_id = models.PositiveIntegerField(null=False, blank=False)

class Employee(Staff):
    employee_id = models.PositiveIntegerField(null=False, blank=False)
    leave_available = models.SmallIntegerField(default=14)
    my_manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)

class Admin(Staff):
    admin_id = models.PositiveIntegerField(null=False, blank=False)
