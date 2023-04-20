from django import forms
from . models import Bill
from .models import Receipts
from .models import Account

#custom date widget
class DateInput(forms.DateInput):
    input_type = 'date'

class AddNewBill(forms.ModelForm):
    class Meta:
        model=Bill
        fields=('clientname','project_cost',)


class CreateReceipt(forms.ModelForm):
    class Meta:
        model=Receipts
        fields=('invoice','transaction_date','amt_paid','payment_mode',)

class AddClient(forms.ModelForm):
    town= forms.CharField(label='Town', required=False)
    county= forms.CharField(label='County',required=True)
    start_date=forms.DateTimeField(label='Start Date',widget=DateInput)
    golive_date=forms.DateField(label='Go-Live Date',widget=DateInput)
    end_date=forms.DateField(label='End Date',widget=DateInput)
    class Meta:
        model=Account
        fields=('town','county','start_date','golive_date','end_date')
