from django.forms import ModelForm
from .models import Student

class EditForm(ModelForm):
    class Meta:
        model=Student
        fields=['surname','name','age']