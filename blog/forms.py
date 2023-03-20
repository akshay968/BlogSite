from django import forms
from .models import Comment
class commentform(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['post']
        labels={
            "user_name":"Your Name",
            "emaild":"Your Email ID",
            "comment":"write the comment here",
        }