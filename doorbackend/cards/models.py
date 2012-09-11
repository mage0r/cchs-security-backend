from django.db import models

# Create your models here.

class Card(models.Model):
	tag_uid = models.CharField(max_length=16)
	owner = models.CharField(max_length=256)
	revoked = models.BooleanField()

class CardEvent(models.Model):
	tag_uid = models.CharField(max_length=16)
	status = models.SmallIntegerField()
	time = models.DateTimeField(auto_now=True)
