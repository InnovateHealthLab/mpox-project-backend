from django.db import models

# Create your models here.
class NewCase(models.Model):
    case_code = models.CharField(max_length=9, null=True, blank=True)
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=6, choices=(('male','Male'),('female','Female')))
    date = models.DateField(auto_now_add=True)
    outcome = models.CharField(max_length=10, choices=(('suspended','Suspended'),('confirmed','Confirmed')))
    test_status = models.CharField(max_length=20, choices=(('pending','Pending'),('confirmed positive','Confirmed Positive'),('confirmed negative','Confirmed Negative')))
    location = models.CharField(max_length=30, null=True, blank=True, help_text='City, Country')
    additional_information = models.TextField(help_text='Occupation, Travel History')