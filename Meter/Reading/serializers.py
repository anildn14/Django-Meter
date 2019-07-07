from rest_framework import serializers
from .models import Meter,Data

class DataSerializer(serializers.ModelSerializer):
	class Meta:
		model=Data
		fields='__all__'

class MeterSerializer(serializers.ModelSerializer):
	datas=DataSerializer(many=True,read_only=True)
	class Meta:
		model=Meter
		fields=('meter_id','datas')


	def create(self, validated_data):
		"""
		Create and return a new `Snippet` instance, given the validated data.
		"""
		return Meter.objects.create(**validated_data)
