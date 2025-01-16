from django import forms
from .models import VPS


class VPSForm(forms.ModelForm):
    class Meta:
        model = VPS
        fields = ['cpu', 'ram', 'hdd', 'status']