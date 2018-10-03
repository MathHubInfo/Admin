from django.shortcuts import redirect, render

from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth import views, decorators
from django.contrib import auth

def admin_template_context(request):
    """ Generates context to be used by the admin forms """
    return {
        'site_title': 'MathHub Admin', 
        'site_header': 'MathHub Admin',
        'username': request.user.get_username(),
        'has_permission': True,
    }

@decorators.login_required
def index(request):
    """ Renders the index page """
    context = {
        'title': 'MathHub Admin', 
        'is_staff': request.user.is_staff
    }
    context.update(admin_template_context(request))
    return render(request, 'mhadmin/index.html', context=context)

class LoginView(views.LoginView):
    template_name = 'admin/login.html'

def login(request):
    """ Renders a login form for a normal user """
    return LoginView.as_view(extra_context=admin_template_context(request))(request)

class LoginStaffView(LoginView):
    authentication_form = AdminAuthenticationForm

def login_staff(request):
    """ Renders a login form for a staff user """
    return LoginStaffView.as_view(extra_context=admin_template_context(request))(request)

@decorators.login_required
def logout(request):
    """ Renders a logout form """
    
    auth.logout(request)
    return redirect('index')