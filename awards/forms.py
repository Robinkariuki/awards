from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','user_project_id']



class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('design','usability','content')