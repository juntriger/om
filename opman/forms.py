from django import forms
from opman.models import Mention

class MentionForm(forms.ModelForm):
    class Meta:
        model = Mention
        fields = ['content']
        labels = {
            'content': 'mention',
        }