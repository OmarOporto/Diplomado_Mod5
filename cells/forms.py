from django import forms
from .models import cells

class cellsForm(forms.ModelForm) :
    class Meta:
        model = cells
        fields = "__all__"