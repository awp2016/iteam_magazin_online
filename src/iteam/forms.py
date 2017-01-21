from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(label="Comment", widget=forms.Textarea, required=True, max_length=500)
