from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.urls import reverse_lazy
from .models import Account
from django.contrib.auth.models import User


class AccountCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', )     # , 'role')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Password don't match")
            return password2
        raise forms.ValidationError('You should write passwords')

    def save(self, commit=True):
        account = super().save(commit=False)
        account.set_password(self.cleaned_data['password1'])
        if commit:
            account.save()
        return account


class AccountChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'image', 'role', 'bio',
                  'is_active', 'is_staff', 'is_superuser')

    def __init__(self, *args, **kwargs):
        super(AccountChangeForm, self).__init__(*args, **kwargs)
        self.fields['password'].help_text = '<a href="%s">change password</a>.' % reverse_lazy(
            'admin:auth_user_password_change', args=[self.instance.id])

    def clean_password(self):
        return self.initial['password']

#
# class AccountLoginForm(forms.ModelForm):
#     class Meta:
#         model = Account
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({
#             "type": "text",
#             "class": "form-input",
#             "name": "name",
#             "id": "name",
#             "placeholder": "Username"
#         })
#
#         self.fields['password'].widget.attrs.update({
#             "type": "text",
#             "class": "form-input",
#             "name": "password",
#             "id": "password",
#             "placeholder": "Password"
#         })
#
#
# class AccountLoginNewForm(forms.ModelForm):
#     class Meta:
#         model = Account
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({
#             "type": "text",
#             "class": "registration-form-field",
#             "name": "username",
#             "aria-label": "First name",
#             "placeholder": "Username",
#             "required": True,
#         })
#
#         self.fields['password'].widget.attrs.update({
#             "type": "password",
#             "class": "registration-form-field",
#             "name": "password",
#             "aria-label": "password",
#             "placeholder": "password",
#         })
