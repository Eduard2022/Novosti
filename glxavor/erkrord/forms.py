from django import forms
from .models import Post,  Comment
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }




class ThreadForm(forms.Form):
  username = forms.CharField(label='', max_length=100)
class MessageForm(forms.Form):
  message = forms.CharField(label='', max_length=1000)