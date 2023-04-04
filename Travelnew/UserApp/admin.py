from django.contrib import admin
from . import models
from . models import Register
from . models import Contact
# Register your models here.
admin.site.register(Register)
admin.site.register(Contact)
