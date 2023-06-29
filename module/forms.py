from django import forms
from .models import Module

class NewModuleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
    hours = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)

    class Meta:
        model = Module
        fields = ['title', 'hours']