from django.db import models

# Create your models here.

# creating company model
class Company(models.Model):
    Company_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    locations=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=
                          (('IT','IT'),
                           ('Non IT','Non IT'),
                           ('AI','AI'),
                           ("Mobile Phones",'Mobile Phones')
                           )) 
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
#Employee Module.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.IntegerField(max_length=10)
    about=models.TextField()
    postion=models.CharField(max_length=100,choices=(
        ('Manager','Manager'),
        ('Software Developer','sd'),
        ('Project Leader','pl'),
        ('Chief Executive Officer','CEO')
    ))
    company=models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employees")