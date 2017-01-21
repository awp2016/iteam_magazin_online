from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from iteam.models import User


class CommentForm(forms.Form):
    text = forms.CharField(label="Comment", widget=forms.Textarea, required=True, max_length=500)


class SearchForm(forms.Form):
    text = forms.CharField(label="", widget=forms.TextInput, required=False, max_length=50)


class UserCreationCustomForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
