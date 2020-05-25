# Generated by Django 3.0.6 on 2020-05-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureHealth', '0038_patientregistrationdatas_insurance'),
    ]

    operations = [
        migrations.CreateModel(
            name='insuranceCompanyLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=200)),
                ('hospital_name', models.TextField()),
            ],
        ),
    ]