from django.contrib import admin
from .models import Secretary, User, Manager, Guest, Appointment
# Register your models here.

admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Secretary)
admin.site.register(Guest)
admin.site.register(Appointment)
