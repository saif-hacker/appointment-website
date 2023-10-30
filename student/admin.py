from django.contrib import admin
from .models import ContactModel


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'fname',
        'lname',
        'email',
        'phone',
    ]
    

# Register your models here.
# admin.site.register(ContactModel)
