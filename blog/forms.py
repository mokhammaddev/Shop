from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "class": "col-lg-6",
            "type": "text",
            "placeholder": "Name"
        })
        self.fields['email'].widget.attrs.update({
            "class": "col-lg-6",
            "type": "text",
            "placeholder": "Email"
        })
        self.fields['message'].widget.attrs.update({
            "class": "col-lg-12",
            "placeholder": "Message"
        })

