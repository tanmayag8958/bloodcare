from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserDetails, HospitalDetails, BankDetails, Address, DoantionLogDetails


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Name')
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']


class User_Details(forms.ModelForm):
    CHOICES = [('A+', 'A+'),
               ('A-', 'A-'),
               ('B+', 'B+'),
               ('B-', 'B-'),
               ('O+', 'O+'),
               ('O-', 'O-'),
               ('AB+', 'AB+'),
               ('AB-', 'AB-')
               ]
    blood_type = forms.ChoiceField(label='Blood Type', choices=CHOICES, required=True)
    contact_no = forms.IntegerField()
    aadhar = forms.CharField(required=True)

    class Meta:
        model = UserDetails
        fields = ['contact_no', 'aadhar', 'blood_type']


class Hospital_Details(forms.ModelForm):
    contact_no = forms.IntegerField()
    MICID = forms.CharField(required=True, label='MCI ID (Medical Council of India)')

    class Meta:
        model = HospitalDetails
        fields = ['contact_no', 'MICID']


class Bank_Details(forms.ModelForm):
    a_positive = forms.IntegerField()
    a_negative = forms.IntegerField()
    b_positive = forms.IntegerField()
    b_negative = forms.IntegerField()
    o_positive = forms.IntegerField()
    o_negative = forms.IntegerField()
    ab_positive = forms.IntegerField()
    ab_negative = forms.IntegerField()
    contact_no = forms.IntegerField()
    MICID = forms.CharField(required=True, label='MCI ID (Medical Council of India)')

    class Meta:
        model = BankDetails
        fields = ['a_positive', 'a_negative', 'b_positive',
                  'b_negative', 'o_positive', 'o_negative', 'ab_positive', 'ab_negative', 'contact_no', 'MICID']

class Address_(forms.ModelForm):
    address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zipcode = forms.CharField()

    class Meta:
        model = Address
        fields = ['address', 'city', 'state', 'zipcode']


class Donate(forms.ModelForm):
    amount = forms.IntegerField()
    CHOICES = [('A+', 'A+'),
               ('A-', 'A-'),
               ('B+', 'B+'),
               ('B-', 'B-'),
               ('O+', 'O+'),
               ('O-', 'O-'),
               ('AB+', 'AB+'),
               ('AB-', 'AB-')
               ]
    blood_type = forms.ChoiceField(label='Blood Type', choices=CHOICES, required=True)

    class Meta:
        model = DoantionLogDetails
        fields = ['amount', 'blood_type']


