from django.db import models

# Create your models here.

class Study(models.Model):
	name = models.CharField(max_length=10)
	stepwise = models.BooleanField()
	no_steps = models.IntegerField(blank=True, null=True)
	randyn = models.BooleanField()
	randq = models.CharField(max_length=20, blank=True)
	
	def __str__(self):
		return self.name	

class GroupSet(models.Model):
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name

class Group(models.Model):
	name = models.CharField(max_length=50)
	groupset = models.ForeignKey(GroupSet, on_delete=models.SET_NULL, null=True)
	No_subjects = models.IntegerField()
	
	def __str__(self):
		return self.name
		
class SampleType(models.Model):
	name = models.CharField(max_length=3)
	full_name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name

class VisitType(models.Model):
	name = models.CharField(max_length=20)
	
	def __str__(self):
		return self.name

class Visit(models.Model):
	order = models.IntegerField()
	type = models.ForeignKey(VisitType, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=20, blank=True)
	number = models.IntegerField(blank=True)
	timepoint = models.CharField(max_length=5, blank=True)
	has_vac = models.BooleanField(blank=True)
	sample = models.CharField(max_length=20, blank=True)
	groupset = models.ForeignKey(GroupSet, on_delete=models.SET_NULL, null=True, blank=True)
	SampleType = models.ManyToManyField(SampleType, blank=True)
	
	def __str__(self):
		return self.name
		

		


