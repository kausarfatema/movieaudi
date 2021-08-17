from allauth.account.adapter import DefaultAccountAdapter
from django.http import HttpResponseRedirect
from django.urls import reverse
class NoNewUsersAccountAdapter(DefaultAccountAdapter):

    def is_auto_signup_allowed(self, request,sociallogin):
        
        return False

    def get_login_redirect_url(self, request):
    	if request.user.is_staff:
    		return reverse("admin_panel")
    	else:
    		return reverse("/")