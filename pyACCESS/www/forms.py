from django import forms

class JobnumForm(forms.Form):
    jobnum = forms.CharField(label='EMS Job Number', max_length=6)