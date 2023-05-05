from django import forms
from . models import support
from .models import courtesy
from .models import bimonthly
from accounts.models import Receipts


#custom date widget
class DateInput(forms.DateInput):
    input_type = 'date'

class AddNewClient(forms.ModelForm):
    logdate=forms.DateTimeField(label='Date',widget=DateInput)
    completiondate=forms.DateTimeField(label='Date',widget=DateInput)
    class Meta:
        model=support
        fields=('__all__')

class AddCourtesyCall(forms.ModelForm):
    logdate=forms.DateTimeField(label='Date',widget=DateInput)
    class Meta:
        model=courtesy
        fields=('__all__')

class AddBimonthlyCall(forms.ModelForm):
    logdate=forms.DateTimeField(label='Date',widget=DateInput)
    class Meta:
        model=bimonthly
        fields=('__all__')