from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import View
from .models import Meter,Data

# #RESTAPI
from .serializers import DataSerializer,MeterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

class DataViewSet(viewsets.ModelViewSet):
	
	queryset=Data.objects.all()
	serializer_class=DataSerializer
	# permission_classes = [AllowAny]

	def get_permissions(self):
		print ("self.action :",self.action)
		if self.action == 'list':					#list all waterparks
			permission_classes = [AllowAny]
		elif self.action == 'create':				#create a new waterpark
			permission_classes = [AllowAny]
			# permission_classes = [IsAdminUser]
		elif self.action == 'retrieve':				#list a single waterpark
			permission_classes = [AllowAny]
		elif self.action == 'update':				#update a waterpark but have to send all the data
			permission_classes = [AllowAny]
			# permission_classes = [IsAdminUser]
		elif self.action == 'partial_update':		#update a waterpark but can send single data
			permission_classes = [AllowAny]
			# permission_classes = [IsAdminUser]
		elif self.action == 'destroy':				#delete a waterpark
			permission_classes = [AllowAny]
			# permission_classes = [IsAdminUser]
		elif self.action == 'hello':
			permission_classes = [AllowAny]
		else:
			permission_classes = [AllowAny]
		return [permission() for permission in permission_classes]

class MeterViewSet(viewsets.ModelViewSet):
	serializer_class = MeterSerializer
	queryset = Meter.objects.all()
	def get_permissions(self):
		print ("self.action :",self.action)
		if self.action == 'list':					#list all waterparks
			permission_classes = [AllowAny]
		elif self.action == 'create':				#create a new waterpark
			permission_classes = [AllowAny]
			# permission_classes = [IsAdminUser]
		elif self.action == 'retrieve':				#list a single waterpark
			permission_classes = [AllowAny]
		elif self.action == 'update':				#update a waterpark but have to send all the data
			permission_classes = [AllowAny]
			# permission_classes = [IsAdminUser]
		elif self.action == 'partial_update':		#update a waterpark but can send single data
			permission_classes = [AllowAny]
			# permission_classes = [IsAdminUser]
		elif self.action == 'destroy':				#delete a waterpark
			permission_classes = [AllowAny]
			# permission_classes = [IsAdminUser]
		elif self.action == 'hello':
			permission_classes = [AllowAny]
		else:
			permission_classes = [AllowAny]
		return [permission() for permission in permission_classes]

class IndexView(generic.ListView):
	template_name="Reading/index.html"
	context_object_name="reading_list"

	def get_queryset(self):
		return Meter.objects.order_by('meter_id')

class DetailView(generic.DetailView):
	model=Meter
	template_name="Reading/detail.html"
	context_object_name="meterid"