from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.models import User

from .models import Profile

# from .models import Profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))


class UserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    password2 = forms.CharField(label='confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    
class ProfileForm(forms.ModelForm):
    choices_c = [("direction", "Human Ressources"), ("network", "Network"), ("sales", "Commercial & Marketing"), ("finance", "Finance")]
    department = forms.ChoiceField(choices = choices_c, widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    class Meta:
        model = Profile
        fields = ('department',)