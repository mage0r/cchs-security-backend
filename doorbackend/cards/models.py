from django.db import models
from datetime import datetime
# Create your models here.

class Card(models.Model):
	tag_uid = models.CharField(max_length=16,unique=True)
	keyA = models.CharField(max_length=32)
	keyB = models.CharField(max_length=32)
	owner = models.IntegerField(default=-1)
	counter = models.PositiveIntegerField(default=0xffffffff)
	revoked = models.BooleanField(default=True)

	def __str__(self):
		return self.tag_uid + " (owner " + str(self.owner) + " revoked: " + str(self.revoked) + ")"

class CardEvent(models.Model):
	tag_uid = models.CharField(max_length=16)
	status = models.SmallIntegerField()
	time = models.DateTimeField(auto_now=True)
	counter = models.PositiveIntegerField()

	def __str__(self):
		return self.tag_uid + " " + self.time.isoformat() + " status: " + str(self.status)
