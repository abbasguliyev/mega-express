from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from account.models import User, UserType, CustomerID

admin.site.register(User)
admin.site.register(UserType)
admin.site.register(CustomerID)

