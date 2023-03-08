from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.models import TimeStampedModel

class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_secretary = models.BooleanField(default=False)
    def __str__(self):
        return self.rank + " / " + self.first_name + " " + self.last_name

class Manager(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    job = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.user.__str__()


class Secretary(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    manager = models.OneToOneField(Manager, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__()


class Guest(TimeStampedModel):

    name = models.CharField(unique=True,max_length=150)
    job = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.rank + " / " + self.name



class Appointment(TimeStampedModel):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    secretary = models.ForeignKey(Secretary, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default="wait")
    purpose = models.CharField(max_length=150, null=True, blank=True)
    comming_date = models.DateTimeField(auto_now_add=True)
    delayed_date = models.DateTimeField(blank=True, null=True)
    left = models.BooleanField(default=False)
    def __str__(self):
        return self.guest.__str__()
