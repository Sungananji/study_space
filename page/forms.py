from django import forms
from .models import Page
from ckeditor.widgets import CKEditorWidget


class NewPageForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)    
    content = forms.CharField(widget=CKEditorWidget)
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Page
        fields = ['title', 'content', 'files', ]
