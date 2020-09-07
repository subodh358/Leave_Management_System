from django.db import models
from core.models import Employee

# Create your models here.
statuses = [('approved', 'approved'),
('declined', 'declined'),
('pending', 'pending'),
('viewed', 'viewed'),
('inprocess', 'inprocess'),
('notviewed', 'notviewed')
]

class LeaveApplication(models.Model):
    start_date = models.DateField(auto_now=False, auto_now_add= False)
    end_date = models.DateField(auto_now_add=False,  auto_now=False)
    description = models.CharField(max_length=100 ,blank=False, null=False)
    status = models.CharField(max_length=20, choices=statuses, default="notviewed")
    author = models.ForeignKey(Employee, on_delete= models.CASCADE)


