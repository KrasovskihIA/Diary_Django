from dataclasses import fields
from django import forms
from .models import Journal

class JournalForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields = ['title', 'description', ]
        labels = {
            'title': 'Введите заголовок',
            'description': 'Введите текст'
        }
