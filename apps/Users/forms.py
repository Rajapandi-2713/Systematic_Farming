from django import forms
from .models import User

class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your email',
            'required': 'required',
            'name': 'email',
            'type':'email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'password',
            'placeholder': 'Enter your password',
            'required': 'required',
            'name': 'password',
        })
    )

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('fullname', 'email', 'password', 'profile')
        widgets = {
        'fullname': forms.TextInput(attrs={
            'placeholder': 'Enter your Fullname',
            'required': 'required',
            'name': 'fullname',
            'type':'text'
        }),
        'email': forms.TextInput(attrs={
            'placeholder': 'Enter your email',
            'required': 'required',
            'name': 'email',
            'type':'email'
        }),

        'password': forms.PasswordInput(attrs={
            'class': 'password',
            'placeholder': 'Enter your password',
            'required': 'required',
            'name': 'password',
        }),

        'profile' :forms.FileInput(attrs = { 
        'id':'formFile',
        'name':'profile',
        'required':'required'
        })
        }
        error_messages = {
            'fullname': {
                'required': 'Please enter your full name.',
            },
            'email': {
                'required': 'Please enter your email address.',
                'invalid': 'Please enter a valid email address.',
            },
            'password': {
                'required': 'Please enter your password.',
            },
            'profile': {
                'required': 'Please upload your profile image.',
            },
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 4:
            raise forms.ValidationError("Password must be at least 4 characters long.")
        return password
    

class EmailForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your email',
            'required': 'required',
            'name': 'email',
            'type':'email'
        })
    )

class OTPForm(forms.Form):
    otp = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your OTP',
            'required': 'required',
            'name': 'otp',
            'type':'text'
        })
    )


class PasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'password',
            'placeholder': 'New password',
            'required': 'required',
            'name': 'password',
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'password',
            'placeholder': 'Confirm password',
            'required': 'required',
            'name': 'confirm_password',
        })
    )