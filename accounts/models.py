from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
# Create your models here.
class Province(models.Model):
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name;

class District(models.Model):
	name=models.CharField(max_length=100)
	province=models.ForeignKey(Province,on_delete=models.CASCADE)
	def __str__(self):
		return self.name;


class Sector(models.Model):
	name=models.CharField(max_length=100)
	district=models.ForeignKey(District, on_delete=models.CASCADE)

	def __str__(self):
		return self.name;



class User(AbstractUser):
	
	RECRUTER='RC'
	TALENT='TL'
	PHOTOGRAPHER='PH'
	UNKNOWN='UN'
	TYPE_IN_CHOICES=[
		(RECRUTER,'Recruter'),
		(TALENT,'Talent'),
		(PHOTOGRAPHER,'Photographer'),
		(UNKNOWN,'Unknown'),

	]
	type_in_choices=models.CharField(
		max_length=2,
		choices=TYPE_IN_CHOICES,
		default=UNKNOWN,
		)
	province=models.ForeignKey(Province,on_delete=models.CASCADE,null=True)
	district=models.ForeignKey(District,on_delete=models.CASCADE,null=True)
	sector=models.ForeignKey(Sector,on_delete=models.CASCADE,null=True)



class Category(models.Model):
	name=models.CharField(max_length=100)
	img=models.ImageField(null=True,upload_to='cat',default='thumb_photos.png')
	
	def __str__(self):
		return self.name

class Recruter(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	company_name=models.CharField(max_length=100,null=True)
	company_address=models.CharField(max_length=100,null=True)
	originated_country=models.CharField(max_length=100,null=True)
	

	def __str__(self):
		return self.user.username + 'Recruter'


class Talent(models.Model):
	
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	category=models.ManyToManyField(Category)
	profile_picture=models.ImageField(upload_to='profile_picture',default='thumb_photos.png')

	def __str__(self):
		return self.user.username + 'Talent'

class Photographer(models.Model):
	talents=models.ManyToManyField(Talent,through='Appointment')
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	cv=models.FileField(upload_to='cvs',default=None)
	is_employed=models.BooleanField(default=False)

	def __str__(self):
		return self.user.username + 'Photographer'


class PhotoImage(models.Model):
	photographer=models.ForeignKey(Photographer,on_delete=models.CASCADE)
	image=models.ImageField(upload_to='photographer_image')



class Appointment(models.Model):
	photographers=models.ForeignKey(Photographer,on_delete=models.CASCADE)
	talent=models.ForeignKey(Talent,on_delete=models.CASCADE)
	status=models.BooleanField(default=False)



# Create your models here.
