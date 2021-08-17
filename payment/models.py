from django.db import models
from accounts.models import Photographer, Talent, Appointment
# Create your models here.

class Payment(models.Model):
	photographer=models.ForeignKey(Photographer,on_delete=models.CASCADE)
	talent=models.ForeignKey(Talent,on_delete=models.CASCADE)
	appointment=models.OneToOneField(Appointment,on_delete=models.CASCADE)



# Create your models here.
