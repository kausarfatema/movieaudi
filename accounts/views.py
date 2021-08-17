from django.shortcuts import render, redirect, get_object_or_404
from .UserRegistration import UserRegisterForm, PhotographerForm, TalentForm, VideoForm
from django.contrib.auth import authenticate, login
from .models import User, Province,District, Sector, PhotoImage
from django.http import JsonResponse, FileResponse
import os
import tempfile
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import moviepy.editor as mp
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .models import Photographer,User,PhotoImage

# Create your views here.
def home(request):
	return render(request,"registration.html")

def admin_panel(request):
	return render(request,"index.html")

def landing(request):
	return render(request,"landing.html")


@unauthenticated_user
def photographereg(request):
	if request.method=='POST':
		u_form=UserRegisterForm(request.POST)
		p_form=PhotographerForm(request.POST, request.FILES)
		if(u_form.is_valid() and p_form.is_valid()):
			u_form.instance.type_in_choices='PH'
			u_form.save()
			p_form.instance.user=u_form.instance
			p_form.save()
			new_user=authenticate(username=u_form.cleaned_data['username'],password=u_form.cleaned_data['password1'])
			login(request,new_user)
			return redirect('upload-apply')
		else:
			context={
		'u_form': u_form,
		'p_form': p_form 
		}

	else:
		u_form=UserRegisterForm()
		p_form=PhotographerForm()
		context={
		'u_form': u_form,
		'p_form': p_form 
		}
	return render(request,"registerphoto.html",context)


def talentreg(request):
	if request.method=='POST':
		u_form=UserRegisterForm(request.POST)
		t_form=TalentForm(request.POST,request.FILES)
		if(u_form.is_valid() and t_form.is_valid()):
			u_form.instance.type_in_choices='TL'
			u_form.save()
			t_form.instance.user=u_form.instance
			t_form.save()
			return redirect('home')
		else:
			context={
		'u_form': u_form,
		't_form': t_form,
		}

	else:
		u_form=UserRegisterForm()
		t_form=TalentForm()
		context={
		'u_form': u_form,
		't_form': t_form ,
		}
	return render(request,"registertalent.html",context)



def validate_username(request):
    username = request.POST.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    print(username)
    return JsonResponse(data)

def load_cities(request):
	province_id=request.GET.get('province_id')
	districts=District.objects.filter(province_id=province_id)
	return render(request,'dis_dropdown.html',{'districts':districts})


def load_districts(request):
	district_id=request.GET.get('district_id')
	sectors=Sector.objects.filter(district_id=district_id)
	return render(request,'sec_dorpdown.html',{'sectors':sectors})

def downloadfile(request):
	if request.method=='POST':
		fs=FileSystemStorage(location='/media')
		v_form=VideoForm(request.POST, request.FILES)
		vid=request.FILES['video']
		file_name1=default_storage.save(vid.name,vid)
		file1=default_storage.open(file_name1)
		file_url1=default_storage.url(file_name1)
		print(file_url1)
		url1_now="http://127.0.0.1:8000"+file_url1
		clip=mp.VideoFileClip(url1_now)
		clip_mp4=clip.write_videofile("F:\\Audition\\media\\test.mp4")



	else:
		v_form=VideoForm()	
	context={
			'v_form':v_form
		}
	return render(request,'edit.html',context)

@login_required
def create_photo(request):
	if request.method=='POST':
		length=request.POST.get('length')

		for filenum  in range(0, int(length)):
			PhotoImage.objects.create(
				photographer=request.user.photographer,
				image=request.FILES.get(f'image{filenum}'))
	return render(request,'upload_file.html')


def viewphotographerapplications(request):
	photographers=Photographer.objects.filter(is_employed=False)
	context={
		'photographers':photographers

	}
	return render(request,'tables.html',context)


def viewphotodetail(request,id):
	photographer=get_object_or_404(Photographer,pk=id)
	photo=PhotoImage.objects.filter(photographer=photographer)

	return render(request,'viewphotodetail.html',{'photo':photo,'photographer':photographer})



	

