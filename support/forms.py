from django import forms
from . models import support
from .models import courtesy
from .models import bimonthly
from accounts.models import Receipts


#custom date widget
class DateInput(forms.DateInput):
    input_type = 'date'

class AddNewClient(forms.ModelForm):
    
    class Meta:
        model=support
        fields=('__all__')

class AddCourtesyCall(forms.ModelForm):
    
    class Meta:
        model=courtesy
        fields=('__all__')

class AddBimonthlyCall(forms.ModelForm):
    
    class Meta:
        model=bimonthly
        fields=('__all__')