from django import forms

class Status_Form(forms.Form):
    attrs = {
        'type': 'text',
        'class': 'status_form',
        'placeholder':'What are you thinking today?',
    }
    status = forms.CharField(label='', required=True, max_length=140, widget=forms.Textarea(attrs=attrs))
