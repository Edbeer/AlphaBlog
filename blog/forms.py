from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class BlogForm(forms.Form):
    title = forms.CharField(max_length=150, label='Title', widget=forms.TextInput(attrs={"class": "form-control"}))
    slug = forms.SlugField(max_length=150, label='URL', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Content', required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
    photo = forms.ImageField(label='IMG', required=False)
    is_published = forms.BooleanField(label='Published', initial=True)

