from django.urls import path, include
from . import views

urlpatterns=[
	path('producer/',views.categorylist, name='category-list')
]