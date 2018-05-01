from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class MHAdminSite(AdminSite):
    site_title = ugettext_lazy('Django Admin')
    site_header = ugettext_lazy('Django Admin')
    index_title = ugettext_lazy('Site administration')

admin_site = MHAdminSite()
admin_site.register(User, UserAdmin)