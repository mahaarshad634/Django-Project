from django.contrib import admin
from myapp.models import ContactMessage,post
# Register your models here.



@admin.register(ContactMessage,post)
class ContactMessageAdmin(admin.ModelAdmin):
   
    pass

