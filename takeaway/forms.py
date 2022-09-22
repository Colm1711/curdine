from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """
    Review form class. Renders body field to screen for user.
    """
    class Meta:
        model = Review
        fields = ['body', ]
