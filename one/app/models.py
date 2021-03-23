from django.db import models

# Create your models here.

class Persons(models.Model):
	"""docstring for Persons"""
	titles= (('manager', 'manager'), ('accountant', 'accountant'), ('technical', 'technical'))
	name = models.CharField(max_length=50)
	age = models.DecimalField(max_digits=2, decimal_places=0)
	email = models.EmailField()
	job_title = models.CharField(max_length=50, choices= titles)


	def __str__(self):
		return self.name
