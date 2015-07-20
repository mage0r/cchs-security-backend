from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Card(models.Model):
	tag_uid = models.CharField(max_length=16,unique=True)
	keyA = models.CharField(max_length=32)
	keyB = models.CharField(max_length=32)
	owner = models.IntegerField(default=-1)
	user = models.ForeignKey(User, null=True, blank=True)
	counter = models.PositiveIntegerField(default=0xffffffff)
	revoked = models.BooleanField(default=True)

	def __str__(self):
		if (self.revoked):
			return self.tag_uid + " (Card Inactive | " + str(self.user) + ")"
		else:
			return self.tag_uid + " (owner: " + str(self.owner) + " User:" + str(self.user)+ ")"

class CardEvent(models.Model):
	tag_uid = models.CharField(max_length=16)
	status = models.SmallIntegerField()
	time = models.DateTimeField(auto_now=True)
	counter = models.PositiveIntegerField()

	def __str__(self):
		return self.tag_uid + " " + self.time.isoformat() + " status: " + str(self.status)

