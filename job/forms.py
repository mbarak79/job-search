from django import forms

from .models import Candidate, Job, Candidate, Resume, User



class CandidateForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['username', 'email']


class JobForm(forms.ModelForm):
    
    class Meta:
        model = Job
        fields = ['title', 'description', 'job_type', 'vacancy', 'salary', 'experience', 'image', 'country', 'city']



class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume

        fields = ['name', 'email', 'url', 'cv', 'cover_letter']




class JobSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search Job!',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )

    


       

