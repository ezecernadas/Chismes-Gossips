from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomTextInput(forms.TextInput):
        def __init__(self, *args, **kwargs):
            kwargs.setdefault('attrs', {})#['class'] = 'tu-clase-css-aqui'
            super(CustomTextInput, self).__init__(*args, **kwargs)

class RegisterForm(UserCreationForm):
        username = forms.CharField(widget=CustomTextInput(
        attrs={
            'placeholder':'Usuario',
            'class': 'form-input'},
            
    ))
        email=forms.EmailField(widget=CustomTextInput(
        attrs={
            'placeholder':'Email',
            'class': 'form-input'},
            
    ))
        first_name = forms.CharField(widget=CustomTextInput(
        attrs={
            'placeholder':'Nombre',
            'class': 'form-input'},
            
    ))
        last_name = forms.CharField(widget=CustomTextInput(
        attrs={
            'placeholder':'Apellido',
            'class': 'form-input'},
            
    ))
        password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Contraseña',
            'class': 'form-input'
        }
    ))
        password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Confirmar contraseña',
            'class': 'form-input'
        }
    ))
    
        class Meta:   
            model = User
            fields = ['username','email','first_name','last_name','password1','password2']