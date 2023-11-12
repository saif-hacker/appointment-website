from django.contrib import admin
from .models import ContactModel
from .models import Sign_up

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'fname',
        'lname',
        'email',
        'phone',
    ]
    

# Register your models here.
@admin.register(Sign_up)
class signupAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
    ]
    

