from django.db import models

# Create your models here.

"""
class Firstname(models.Model):
	Firstname = models.CharField(max_length=200)
	Lastname=models.CharField(max_length=200)
"""
class Book(models.Model):
	Bookname=models.CharField(max_length=500)
	Authorname=models.CharField(max_length=500)
	price=models.IntegerField()
"""
class Address(models.Model):
	#docstring for ClassName
	address1 = models.TextField()
	address2 = models.TextField()
	pincode  = models.IntegerField()
	
		
class section(models.Model):
	section_in_class=(
		('A','First'),
		('B','Second'),
		('C','Third')
		)
	sect=models.CharField(max_length=30,choices=section_in_class,default='A')
"""