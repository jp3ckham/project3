# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Asset(models.Model):
    asset_id = models.AutoField(primary_key=True)
    organization_id = models.IntegerField(blank=True, null=True)
    office_id = models.IntegerField(blank=True, null=True)
    manufacturer_id = models.IntegerField(blank=True, null=True)
    part_number = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    date_implemented = models.DateField(blank=True, null=True)
    maint_notes = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Asset'


class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Manufacturer'


class Office(models.Model):
    office_id = models.AutoField(primary_key=True)
    office_location = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Office'


class Organization(models.Model):
    organization_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Organization'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
