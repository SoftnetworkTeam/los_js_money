from django.contrib import admin

from userauth.models import MasterAuth, UserAuth

admin.site.register(MasterAuth)

admin.site.register(UserAuth)
