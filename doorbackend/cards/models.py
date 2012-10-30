from django.db import models

# Create your models here.

class Card(models.Model):
	tag_uid = models.CharField(max_length=16,unique=True)
	keyA = models.CharField(max_length=32)
	keyB = models.CharField(max_length=32)
	owner = models.IntegerField(default=-1)
	counter = models.PositiveIntegerField(default=0xffffffff)
	revoked = models.BooleanField(default=True)

class CardEvent(models.Model):
	tag_uid = models.CharField(max_length=16)
	status = models.SmallIntegerField()
	time = models.DateTimeField(auto_now=True)
	counter = models.PositiveIntegerField()
