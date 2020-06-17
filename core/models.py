from django.db import models

class Professions(models.Model):
	ST = 'ST'
	SE = 'SE'
	WD = 'WD'
	DS = 'DS'
	DA = 'DA'
	OT = 'OT'

	profession_list = {
		(ST, 'Student'),
		(SE, 'Software Enginer'),
		(WD, 'Web Developer'),
		(DS, 'Data Scientiest'),
		(DA, 'Data Analysts'),
		(OT, 'Others')
	}

	profession_name = models.CharField(choices=profession_list, max_length=2)

	def __str__(self):
		return self.profession_name


class Datasheet(models.Model):
	datasheet_name = models.CharField(max_length=50)
	datasheet_text = models.TextField()

	def __str__(self):
		return self.datasheet_name


class Customer(models.Model):
	name = models.CharField(max_length=50, null=False)
	address = models.CharField(max_length=50)
	profession = models.ManyToManyField(Professions)
	datasheet = models.ForeignKey(Datasheet, on_delete=models.CASCADE, null = True)
	active = models.BooleanField(null=True)

	def __str__(self):
		return self.name


class Documents(models.Model):
	PP = 'PP'
	ID = 'ID'
	OT = 'OT'

	DOC_TYPE = {
		(PP, 'Passport'),
		(ID, 'Identity Card'),
		(OT, 'Others')
	}

	documents_type = models.CharField(choices=DOC_TYPE, max_length=2, null=False)
	documents_number = models.CharField(max_length=50)

	def __str__(self):
		return self.documents_number