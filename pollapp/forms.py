from django import forms
from .models import Poll, Choice
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class PollForm(forms.ModelForm):
    end_date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your question here'})
    )
    class Meta:
        model = Poll
        fields = ['title', 'description', 'end_date']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': ' '})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': ' '})
    )

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': ' '}),
        }
        error_messages = {
            'username': {
                'max_length': "Username must be 150 characters or fewer.",
                'invalid': "Only letters, digits, and @/./+/-/_ are allowed in the username.",
                'required': "Username is required. Please enter a valid username."
            },
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password)
        except ValidationError as e:
            self.add_error('password', e)
   
class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': ' '}),
        help_text="Your password must be at least 8 characters long and not entirely numeric.",
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': ' '}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': ' '}),
        }
        error_messages = {
            'username': {
                'max_length': "Username must be 150 characters or fewer.",
                'invalid': "Only letters, digits, and @/./+/-/_ are allowed in the username.",
                'required': "Username is required. Please enter a valid username."
            },
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password)
        except ValidationError as e:
            raise ValidationError(e)
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError({
                'confirm_password': "Passwords do not match. Please try again."
            })

        return cleaned_data
