from django import forms
from .models import Comments


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ' Leave your feedback'}))
    rating = forms.IntegerField(max_value=10, min_value=1)
