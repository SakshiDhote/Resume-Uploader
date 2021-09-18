from django import forms
from .models import ResumeModel

GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
]

JOB_CITY_CHOICE=[
    ('Delhi', 'Delhi'),
    ('Pune', 'Pune'),
    ('Ranchi', 'Ranchi'),
    ('Mumbai', 'Mumbai'),
    ('Dhanbad', 'Dhanbad'),
    ('Banglore', 'Banglore')
]

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=ResumeModel
        fields='__all__'
        # labels={'name':Full Name,'dob'=Date of Birth}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }