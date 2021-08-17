from django.urls import path, include
from . import views

urlpatterns = [
    path('tables/', views.viewphotographerapplications,name='phototable'),
    path('tables/<int:id>',views.viewphotodetail, name="photogr"),
    path('',views.admin_panel,name='admin-panel'),
    ]