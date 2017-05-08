import datetime

from django.db import models
from django.utils import timezone

from authentication.models import Account


class Accountant(models.Model):
    image = models.ImageField(upload_to='profile_images')
    account = models.OneToOneField(Account)
    denomination_social = models.CharField(max_length=50)
    nom_representant = models.CharField(max_length=50)
    lordre_numero = models.CharField(max_length=50)
    tableau_inscrit = models.CharField(max_length=50)
    address = models.TextField()
    code_postale= models.IntegerField()
    ville = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    commentaire = models.TextField()


class Collaborator(models.Model):
    image = models.ImageField(upload_to='profile_images')
    account = models.OneToOneField(Account)
    accountant = models.ForeignKey(Accountant)


class Candidate(models.Model):
    image = models.ImageField(upload_to='profile_images/', default='profile_images/default.jpg')
    account = models.OneToOneField(Account)
    collaborator = models.ForeignKey(Collaborator, null=True)
    birth_date = models.DateField()

    # place of birth
    city_birth = models.CharField(max_length=50)
    department_birth = models.CharField(max_length=50)
    country_birth = models.CharField(max_length=50)

    # address
    address = models.TextField()
    additional_address = models.TextField(blank=True)
    zip_code = models.IntegerField()
    city_address = models.CharField(max_length=50)


class PhysicPerson(models.Model):
    image = models.ImageField(upload_to='profile_images')
    account = models.OneToOneField(Account)
    birth_date = models.DateField(blank=True)
    # place of birth
    city_birth = models.CharField(max_length=50)
    department_birth = models.CharField(max_length=50)
    country_birth = models.CharField(max_length=50)
    # address
    address = models.TextField()
    additional_address = models.TextField()
    zip_code = models.IntegerField()
    city_address = models.CharField(max_length=50)


class MoralPerson(models.Model):
    image = models.ImageField(upload_to='profile_images')
    association_name = models.CharField(max_length=50)

    # address
    address = models.TextField()
    additional_address = models.TextField()
    zip_code = models.IntegerField()
    city_address = models.CharField(max_length=50)

    national_number = models.CharField(max_length=12)


class AccountType(models.Model):
    ACCOUNTANT = 'Expert Comptable'
    COLLABORATOR = 'Collaborateur'
    PHYSICPERSON = 'Mandataire Physique',
    MORALPERSON = 'Mandataire Morale',
    CANDIDATE = 'Candidat'

    types = (
        (CANDIDATE, CANDIDATE),
        (ACCOUNTANT, ACCOUNTANT),
        (COLLABORATOR, COLLABORATOR),
        (PHYSICPERSON, PHYSICPERSON),
        (MORALPERSON, MORALPERSON),
    )
    account = models.OneToOneField(Account)
    type = models.CharField(choices=types, default=types[0][0], max_length=20)

