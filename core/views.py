from django.shortcuts import render
from rest_framework import viewsets
from core.serializer import CustomerSerializer,ProfessionSerializer,DatasheetSerializer,DocumentsSerializer

class CustomerViewSet(viewsets.ModelViewSet):
	serializer_class = CustomerSerializer

	def get_queryset(self):
		active_customer = Customer.objects.filter(active=True)
		return active_customer

	
class ProfessionViewSet(viewsets.ModelViewSet):
	queryset = Professions.objects.all()
	serializer_class = ProfessionSerializer

class DatasheetViewSet(viewsets.ModelViewSet):
	queryset = Datasheet.objects.all()
	serializer_class = DatasheetSerializer


class DocumentsViewSet(viewsets.ModelViewSet):
	queryset = Documents.objects.all()
	serializer_class = DocumentsSerializer