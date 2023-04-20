from django import forms
from . models import BizLead, Demo



#custom date widget
class DateInput(forms.DateInput):
    input_type = 'date'

class AddNewBizleadForm(forms.ModelForm):
    created_date=forms.DateTimeField(label='Date',widget=DateInput)
    class Meta:
        model=BizLead
        fields=('name','town','county','contact_person','contact_phone','comment','created_date')

class AddDemoForm(forms.ModelForm):
    demodate=forms.DateTimeField(label='Demo Date',widget=DateInput,required=False)
    assessmentdate=forms.DateTimeField(label='Assessment Date',widget=DateInput,required=False)
    reportdate=forms.DateTimeField(label='Report Dissemination Date',widget=DateInput,required=False)
    class Meta:
        model=Demo
        fields=('__all__')
