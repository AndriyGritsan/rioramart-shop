from django import forms             
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User


User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-2', 
                                      'placeholder': 'Email'})
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control input-password py-2',
                                          'placeholder': 'Password'})
    )
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.user_cache = None
    
    
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError("There was a problem with your login.")
        return user
        
    
    
    def clean(self):
        cleaned_data = super().clean()
        
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        
        if email and password:
            self.user_cache = authenticate( username=email, password=password)
            
            if self.user_cache is None:
                raise forms.ValidationError('Invalid email or password')
            else:
                self.confirm_login_allowed(self.user_cache)
        return cleaned_data
    
    def get_user(self):
        return self.user_cache
               
  
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control input-password py-2',
            'placeholder': 'Password'
        })
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget= forms.PasswordInput(attrs={
            'class': 'form-control input-password py-2',
            'placeholder': 'Password'
        })
    )
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don`t match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
        
    
    class Meta:
        model = User
        fields = ('email',  )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control py-2', 
                                             'placeholder': 'Email'})
        }
        

class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-2',
                                       'placeholder': 'Email' })
    )
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }