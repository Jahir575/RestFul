# Generated by Django 3.0.7 on 2020-06-16 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200615_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='datasheet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Datasheet'),
        ),
        migrations.AlterField(
            model_name='professions',
            name='profession_name',
            field=models.CharField(choices=[('SE', 'Software Enginer'), ('DA', 'Data Analysts'), ('ST', 'Student'), ('OT', 'Others'), ('DS', 'Data Scientiest'), ('WD', 'Web Developer')], max_length=2),
        ),
    ]