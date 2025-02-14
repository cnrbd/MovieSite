from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})

class CustomPasswordChangeForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    old_password = forms.CharField(widget=forms.PasswordInput, required=True, label='Old Password')
    new_password1 = forms.CharField(widget=forms.PasswordInput, required=True, label='New Password')
    new_password2 = forms.CharField(widget=forms.PasswordInput, required=True, label = 'Confirm New Password')

    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        old_password = cleaned_data.get('old_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            self.add_error('new_password1', 'The new passwords do not match.')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.add_error('username', 'User does not exist.')
            return cleaned_data

        if not check_password(old_password, user.password):
            self.add_error('old_password', 'The old password is incorrect.')

        return cleaned_data

    def save(self):
        username = self.cleaned_data.get('username')
        new_password = self.cleaned_data.get('new_password1')
        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()