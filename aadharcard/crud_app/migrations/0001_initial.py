# Generated by Django 5.0.3 on 2024-03-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AadharCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('mobile_number', models.IntegerField()),
                ('aadhar_no', models.IntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=10)),
            ],
        ),
    ]