from django.db import models
from django.contrib.auth.models import User
from cards.models import Card
from datetime import datetime

# Create your models here.

class Machine(models.Model):
	name = models.CharField(max_length=16,unique=True)
	active = models.BooleanField(default=False)
	LEVELS = (
                ('0', 'Not Cleared'),
                ('1', 'Operator'),
                ('2', 'Instructor'),
        )
	minimum_level = models.CharField(max_length=3,choices=LEVELS, default=0)

	def __str__(self):
                return self.name + " (Active=" + str(self.active) + ")"

	def short(self):
		return self.name

class MachineAccess(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	machine = models.ForeignKey(Machine)
	LEVELS = (
		('0', 'Not Cleared'),
		('1', 'Operator'),
		('2', 'Instructor'),
	)
	level = models.CharField(max_length=3,choices=LEVELS, default=0)

	def __str__(self):
                return self.machine.name + " [" + str(self.user) + ", " + (self.get_level_display()) + "]"
