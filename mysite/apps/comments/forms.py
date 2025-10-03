from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text', 'parent']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام شما'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ایمیل شما'}),
            'text': forms.Textarea(attrs={'class':'form-control', 'placeholder':'متن کامنت'}),
            'parent': forms.HiddenInput()
        }