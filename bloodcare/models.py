from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
import uuid


# Create your models here.

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField('Address', max_length=100)
    city = models.CharField('City', max_length=60)
    state = models.CharField('State',max_length=30)
    zipcode = models.CharField('Zipcode', max_length=6)
    country = models.CharField('Country', max_length=50, default='India')

    def __str__(self):
        return self.user.username


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_registered = models.DateTimeField('Date Registered', default=timezone.now)
    contact_no = models.BigIntegerField('Contact Number', default=91)
    blood_type = models.CharField('Blood Type', max_length=3, null=False)
    aadhar = models.CharField('Aadhar Number', max_length=12, null=False)
    status = models.CharField('Status', max_length=12, default='Active')

    def __str__(self):
        return self.user.username

class HospitalDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_registered = models.DateTimeField('Date Registered', default=timezone.now)
    contact_no = models.BigIntegerField('Contact Number', default=91)
    verify_status = models.CharField('Status', max_length=12, default='Pending')
    MICID = models.CharField('MICID', max_length=50, null=False)

    def __str__(self):
        return self.user.username

class BankDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_registered = models.DateTimeField('Date Registered', default=timezone.now)
    contact_no = models.BigIntegerField('Contact Number', default=91, null=False)
    a_positive = models.IntegerField('A+', default=0)
    a_negative = models.IntegerField('A-', default=0)
    b_positive = models.IntegerField('B+', default=0)
    b_negative = models.IntegerField('B-', default=0)
    o_positive = models.IntegerField('O+', default=0)
    o_negative = models.IntegerField('O-', default=0)
    ab_positive = models.IntegerField('AB+', default=0)
    ab_negative = models.IntegerField('AB-', default=0)
    MICID = models.CharField('MICID', max_length=50, null=False)
    verify_status = models.CharField('Status', max_length=12, default='Pending', null=False)

    def __str__(self):
        return self.user.username

class DoantionLogDetails(models.Model):
    donated_from = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_donated_from', on_delete=models.PROTECT, null=False, default=None)
    donated_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_donated_to', on_delete=models.PROTECT, null=False, default=None)
    unit_id = models.UUIDField('Unit ID', default=uuid.uuid4, editable=True, unique=True, null=False)
    donation_id = models.UUIDField('Donation ID', primary_key=True, default=uuid.uuid4, editable=True, unique=True, null=False)
    blood_type = models.CharField('Blood Type', max_length=3, null=False)
    amount = models.IntegerField('Amount in ml', null=False)

    def __str__(self):
        return self.donated_from.username


class UseLogDetail(models.Model):
    pass






