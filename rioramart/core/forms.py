from django import forms
from .models import MessageUser, Subscription

class MessageUserForm(forms.ModelForm):
    class Meta:
        model = MessageUser
        fields = ('first_name', 'last_name', 'email', 'message')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control bg-light border-0 py-2',
                                                 'placeholder': 'Enter your firstname'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control bg-light border-0 py-2',
                                                'placeholder': 'Enter your  lastname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-light border-0 py-2',
                                             'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control bg-light border-0 py-2',
                                              'placeholder': 'Enter your message'})
        }
        
        
class SubscriptionUserForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('email', )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control w-50', 'placeholder': 'Your email address'})
        }