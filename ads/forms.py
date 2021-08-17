from django import forms
from .models import Ad, Application



class Adform(forms.ModelForm):
	class Meta:
		model=Ad
		exclude=['talents']

class ApplicationForm(forms.ModelForm):
	class Meta:
		model=Application
		exclude=['ads,talents']