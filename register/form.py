from django import forms


class SubscribersForm(forms.Form):
    user_name = forms.CharField(min_length=4, max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(min_length=4, max_length=10,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter email'}))
