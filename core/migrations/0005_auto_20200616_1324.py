# Generated by Django 3.0.7 on 2020-06-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200616_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents_type', models.CharField(choices=[('OT', 'Others'), ('ID', 'Identity Card'), ('PP', 'Passport')], max_length=2)),
                ('documents_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='professions',
            name='profession_name',
            field=models.CharField(choices=[('DA', 'Data Analysts'), ('SE', 'Software Enginer'), ('DS', 'Data Scientiest'), ('WD', 'Web Developer'), ('ST', 'Student'), ('OT', 'Others')], max_length=2),
        ),
    ]