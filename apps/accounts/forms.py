from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('There is someone using this email')
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# class CustomAuthenticationForm(AuthenticationForm):
#     username = forms.CharField(max_length=254)
#     password = forms.CharField(widget=forms.PasswordInput)
#     widgets = {
#         'username': forms.TextInput(attrs={
#             'placeholder':'Nome completo',
#             'class':'form-control',
#             'required':'required',
            
#         }),
#         'password': forms.PasswordInput(attrs={
#             'placeholder':'Nome completo',
#             'class':'form-control',
#             'required':'required',
            
#         }),
#     }
#     def confirm_login_allowed(self, user):
#         if not user.is_active or not user.is_validated:
#             raise forms.ValidationError('There was a problem with your login.', code='invalid_login')