from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordResetForm
# from django.contrib.auth.models import User
from .models import CustomUser


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Name:', 
            'id': 'content', 
            'name':'content',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password:',
            'id': 'content',
            'name':'content',
        }
    ))

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your mail',
        'type': 'email',
        'name': 'email',
        }))

class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "type":"text",
            "name":"content", 
            "id":"content",
            "placeholder":"Name:",
            'required' : "required",
            "class":"form-control"
        })
        self.fields["phone"].widget.attrs.update({
            "class":"form-control",
            "type":"tel",
            "name":"content",
            "id":"content",
            "placeholder":"Phone Number:",
            'required' : "required",
            "class":"form-control"
        })
        self.fields["email"].widget.attrs.update({
            "type":"email", 
            "name":"content", 
            "id":"content",
            "placeholder":"Email:",
            'required' : "required",
            "class":"form-control"
        })
        self.fields["password1"].widget.attrs.update({
            "type":"password", 
            "name":"content",
            "id":"content",
            "placeholder":"Password:",
            'required' : "required",
            "class":"form-control"
            # "label
        })
        self.fields["password2"].widget.attrs.update({
            "type":"password", 
            "name":"content",
            "id":"content",
            "placeholder":"Password Confirmation:",
            'required' : "required",
            "class":"form-control"
            # "label
        })

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'phone',
            'email',
            'password1',
            'password2',
        ]
