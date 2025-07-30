from django import forms
from .models import Job, Application

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'location', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume', 'cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
        }

class JobSearchForm(forms.Form):
    search = forms.CharField(
        max_length=200, 
        required=False, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by job title, company, or location...',
            'class': 'form-control'
        })
    )
