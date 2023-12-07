from django import forms
from .models import Contact, Comment


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["message"].widget.attrs.update({
            "placeholder": "message to leave a comment",
            "class": "col-lg-12 text-center",
        })
