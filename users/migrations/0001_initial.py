# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 08:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accountant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile_images')),
                ('denomination_social', models.CharField(max_length=50)),
                ('nom_representant', models.CharField(max_length=50)),
                ('lordre_numero', models.CharField(max_length=50)),
                ('tableau_inscrit', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('code_postale', models.IntegerField()),
                ('ville', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('commentaire', models.TextField()),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Candidat', 'Candidat'), ('Expert Comptable', 'Expert Comptable'), ('Collaborateur', 'Collaborateur'), (('Mandataire Physique',), ('Mandataire Physique',)), (('Mandataire Morale',), ('Mandataire Morale',))], default='Candidat', max_length=20)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='profile_images/default.jpg', upload_to='profile_images/')),
                ('birth_date', models.DateField(auto_now=True)),
                ('city_birth', models.CharField(max_length=50)),
                ('department_birth', models.CharField(max_length=50)),
                ('country_birth', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('additional_address', models.TextField(blank=True)),
                ('zip_code', models.IntegerField()),
                ('city_address', models.CharField(max_length=50)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile_images')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('accountant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Accountant')),
            ],
        ),
        migrations.CreateModel(
            name='MoralPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile_images')),
                ('association_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('additional_address', models.TextField()),
                ('zip_code', models.IntegerField()),
                ('city_address', models.CharField(max_length=50)),
                ('national_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile_images')),
                ('birth_date', models.DateField(blank=True)),
                ('city_birth', models.CharField(max_length=50)),
                ('department_birth', models.CharField(max_length=50)),
                ('country_birth', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('additional_address', models.TextField()),
                ('zip_code', models.IntegerField()),
                ('city_address', models.CharField(max_length=50)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='collaborator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Collaborator'),
        ),
    ]
