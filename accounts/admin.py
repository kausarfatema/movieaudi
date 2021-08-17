from django.contrib import admin
from .models import User,Photographer,Appointment,Talent,Category,Recruter,Province,District,Sector,PhotoImage
from payment.models import Payment
from .form import GroupAdminForm
from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(User)
admin.site.register(Photographer)
admin.site.register(Talent)
admin.site.register(Appointment)
admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(Recruter)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Sector)
admin.site.register(PhotoImage)
# Register your models here.
admin.site.unregister(Group)

class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

admin.site.register(Group, GroupAdmin)