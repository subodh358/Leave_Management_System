from django.forms import ModelForm
from django.db import models
from .models import LeaveApplication
from core.models import Employee

#form begins from here
statuses = [('approved', 'approved'),
('declined', 'declined'),
('pending', 'pending'),
('viewed', 'viewed'),
('inprocess', 'inprocess'),
('notviewed', 'notviewed')
]
class LeaveApplicationForm(ModelForm):
    start_date = models.DateField(auto_now=False, auto_now_add= False)
    end_date = models.DateField(auto_now_add=False,  auto_now=False)
    description = models.CharField(blank=False, null=False)
    author = models.ForeignKey(Employee, on_delete= models.CASCADE)
    class Meta:
        model = LeaveApplication
        fields = ['start_date', 'end_date', 'description', 'author']

