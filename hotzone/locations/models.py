from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class StaffUser(AbstractUser):
    chpStaffNumber = models.CharField("CHP Staff Number", max_length=7, unique=True)
    '''
    userName = models.CharField(unique=True)
    email = models.EmailField(max_length=255, unique=True)
    firstName = models.CharField()
    lastName = models.CharField()

    USERNAME_FIELD = 'userName'
    #REQUIRED_FIEDS = ['email', 'firstName', 'lastName', 'chpStaffNumber']

    def __str__(self):
        return self.userName
    '''


class Patient(models.Model):
    name = models.CharField(max_length=80, default="")
    idNumber = models.CharField(max_length=20)
    dateOfBirth = models.DateField()

    def __str__(self):
        return f'{self.id}  {self.name}'


class Virus(models.Model):
    name = models.CharField(max_length=30)
    commonName = models.CharField(max_length=50)
    maxInfectiousPeriod = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Viruses'


class Case(models.Model):
    CASE_TYPES = (
        ('Local', 'Local'),
        ('Imported', 'Imported'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    virus = models.ForeignKey(Virus, on_delete=models.CASCADE)
    dateConfirmed = models.DateField()
    caseType = models.CharField(max_length=8, choices=CASE_TYPES)

    def __str__(self):
        return f'{self.patient.name} {self.virus.name}'


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Visit(models.Model):
    VISIT_TYPES =( 
        ("Visit", "Visit"), 
        ("Residence", "Residence"), 
        ("Workplace", "Workplace"), 
    ) 
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    dateFrom = models.DateField()
    dateTo = models.DateField()
    category = models.CharField(max_length=20, choices=VISIT_TYPES)

    def __str__(self):
        return f' {self.case.id} {self.location.name}'
        