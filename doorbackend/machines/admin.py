from django.contrib import admin
from django.contrib import admin
from cards.models import User
from machines.models import Machine,MachineAccess

# Register your models here.
admin.site.register(Machine)
admin.site.register(MachineAccess)
