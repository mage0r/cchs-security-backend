from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserDetail(models.Model):
	user = models.OneToOneField(User)
	address = models.CharField(max_length=64, null=True, blank=True)
	phone_number = models.CharField(max_length=10)

	
	
	def __str__(self):
                return str(self.user) + " [" + self.phone_number + "]"
