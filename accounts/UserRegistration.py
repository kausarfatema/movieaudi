from django import forms
from .models import User,Photographer,Talent,Category,District,Sector,Province, Recruter
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()
	first_name=forms.CharField(max_length=100)
	last_name=forms.CharField(max_length=100)	
	class Meta:
	 	model= User
	 	fields=['username','email','first_name','last_name','password1','password2','province','district','sector']
	 	widget={
			'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
		}
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['district'].queryset=District.objects.none()
		self.fields['sector'].queryset=Sector.objects.none()

		if 'province' in self.data and 'district' in self.data:
			try:
				province_id=int(self.data.get('province'))
				self.fields['district'].queryset=District.objects.filter(province_id=province_id)
				district_id=int(self.data.get('district'))
				self.fields['sector'].queryset=Sector.objects.filter(district_id=district_id)
			except (ValueError,TypeError):
				pass


class PhotographerForm(forms.ModelForm):
	class Meta:
		model=Photographer
		fields=['cv']



class TalentForm(forms.ModelForm):
	category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
	class Meta:
		model=Talent
		exclude=['user']

class RecruterForm(forms.ModelForm):
	class Meta:
		model=Recruter
		exclude=['user']



class VideoForm(forms.Form):
	video=forms.FileField()


		
			