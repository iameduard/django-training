from django.contrib import admin

# Register your models here.
from .models import Book
#from .models import Firstname, Address, section

admin.site.register(Book)
"""
admin.site.register(Firstname)

admin.site.register(Address)

admin.site.register(section)
"""