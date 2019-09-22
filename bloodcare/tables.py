from django_tables2 import tables, TemplateColumn
from .models import DoantionLogDetails, BankDetails


class SimpleTable(tables.Table):
    class Meta:
        model = DoantionLogDetails
        exclude = ('unit_id', 'donation_id')


class BloodType(tables.Table):
    class Meta:
        model = BankDetails
        exclude = ('id', 'user', 'date_registered', 'contact_no', 'MICID', 'verify_status')
        # fields = ('a_positive', 'a_negative')


class BloodTypeSearch(tables.Table):
    class Meta:
        model = BankDetails
        exclude = ('id', 'date_registered', 'MICID', 'verify_status')
