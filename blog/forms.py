from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class ContactForm(forms.Form):
    name = forms.CharField(label='Your name',max_length=100)
    email = forms.EmailField(label='Your email')
    message = forms.CharField(widget=forms.Textarea, label='Message')   
    
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
