from django import forms
from .models import Post

class EditProyectoForm(forms.ModelForm):

    class Meta:
        model = Post