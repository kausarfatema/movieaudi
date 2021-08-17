from django.shortcuts import render, redirect
from .forms import Adform,ApplicationForm
from django.http import JsonResponse
import datetime
from .models import Ad
from accounts.models import Category
# Create your views here.

def testview(request):
	if request.method == 'POST':
		a_form= Adform(request.POST)
		if a_form.is_valid():
			a_form.save()
			return redirect('home')
	else:
		a_form=Adform()
		context={
		'a_form':a_form
		}

	return render(request,'testad.html',context)


def testvalidate(request):
	date=request.POST.get('date',None)
	tr=datetime.datetime.strptime(date,'%m/%d/%Y').strftime('%Y-%m-%d')
	print(tr)
	data={
		'is_appoint': Ad.objects.filter(date=tr).exists()
	}
	return JsonResponse(data)

def categorylist(request):
	category=Category.objects.all()
	context={
	'category':category
	}
	return render(request, 'producer.html', context)


def try_pks(request, pk,pk_alt):
	print(pk + pk_alt)
	return redirect('home')



def apply(request,pk):
	ad=Ad.objects.get(pk=pk)
	if ad.is_past_due():
		return redirect('landing')

	else:
		if request.method=='POST':
			ap_form=ApplicationForm(request.POST)
			if ap_form.is_valid:
				ap_form.instance.talents=request.user.talents
				ap_form.instance.ads=ad
				ap_form.save()
				return redirect('home')
		
		else:
			ap_form=ApplicationForm()
			context={
			'ap_form':ap_form
			}

		return render(request,'',context)



