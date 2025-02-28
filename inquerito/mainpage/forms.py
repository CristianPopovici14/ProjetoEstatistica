from django import forms
from .models import Data

class UploadSurvey(forms.ModelForm):
    socialtime = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'socialtime',
            'name': 'socialtime',
            'placeholder': 'Número em horas',
            'required': True,
        }),
        label="",
    )
    sleeptime = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'sleeptime',
            'name': 'sleeptime',
            'placeholder': 'Número em horas',
            'required': True,
        }),
        label="",
    )

    class Meta:
        model = Data
        fields = ['socialtime', 'sleeptime']
