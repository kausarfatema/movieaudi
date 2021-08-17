from django.db import models

# Create your models here.
from accounts.models import Recruter, Talent, User, Category
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date


class Ad(models.Model):
	name=models.CharField(max_length=100)
	recruter=models.ForeignKey(Recruter,on_delete=models.CASCADE)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	talents=models.ManyToManyField(Talent,through='Application')
	date=models.DateField(default=None)
	
	def __str__(self):
		return self.name

	@property
	def is_past_due(self):
		return date.today() > self.date


class Application(models.Model):
	name=models.CharField(max_length=100)
	talent=models.ForeignKey(Talent, on_delete=models.CASCADE,null=True)
	ads=models.ForeignKey(Ad, on_delete=models.CASCADE)
	video=models.FileField(upload_to="videos/",null=True)
	class Meta:
		unique_together=[['talent','ads']]






