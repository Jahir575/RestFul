# Generated by Django 3.0.7 on 2020-06-15 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datasheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datasheet_name', models.CharField(max_length=50)),
                ('datasheet_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession_name', models.CharField(choices=[('ST', 'Student'), ('SE', 'Software Enginer'), ('DA', 'Data Analysts'), ('DS', 'Data Scientiest'), ('WD', 'Web Developer'), ('OT', 'Others')], max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='documents',
        ),
        migrations.DeleteModel(
            name='Documents',
        ),
        migrations.AddField(
            model_name='customer',
            name='datasheet',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Datasheet'),
        ),
        migrations.AddField(
            model_name='customer',
            name='profession',
            field=models.ManyToManyField(to='core.Professions'),
        ),
    ]
