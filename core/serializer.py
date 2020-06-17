from .models import Professions,Datasheet,Customer,Documents
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ['id','name','address','profession','datasheet', 'active']

class ProfessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Professions
		fields = ['id', 'profession_name']

class DatasheetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Datasheet
		fields = ['id', 'datasheet_name', 'datasheet_text']

class DocumentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Documents
		fields = ['id', 'documents_type', 'documents_number']
