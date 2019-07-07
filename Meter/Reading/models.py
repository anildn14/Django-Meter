from django.db import models
import datetime
from django.utils import timezone

class Meter(models.Model):
	meter_id=models.CharField(max_length=50,primary_key=True)
	
	def __str__(self):
		return str(self.meter_id)

class Data(models.Model):
	class Meta:
		ordering = ['timestamp']
		# ordering = int['sequence_id']

	meter=models.ForeignKey(Meter,related_name='datas',on_delete=models.CASCADE)
	sequence_id = models.CharField(max_length=50,unique=True)
	timestamp = models.DateTimeField(default=datetime.datetime.now())#timezone.now())#datetime.datetime.now())
	CONNECTION_CHOICES=(('Connected','Connected'),('Disconnected','Disconnected'))
	connection_status = models.CharField(max_length=15,choices=CONNECTION_CHOICES)

	def __str__(self):
		return str(self.meter) + ' - ' + str(self.sequence_id)+ ' - ' + str(self.timestamp)+ ' - ' + str(self.connection_status)