from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    
    COUNTRIES = [
            ('', 'Select your Country'),
            ('UK', 'United Kingdom'),
            ('US', 'United States'),
            ('BD', 'Bangladesh'),
            ('AU', 'Australia'),
            ('CA', 'Canada'),
            ('CN', 'China'),
            ('MA', 'Morocco'),
            ('SA', 'Saudi Arabia')
            ]
            
    country = forms.ChoiceField(choices=COUNTRIES, widget=forms.Select(attrs={'class': 'input-item gs_input_area'}))
    shopping_country = forms.ChoiceField(choices=COUNTRIES, widget=forms.Select(attrs={'class': 'input-item gs_input_area w-100'}))     
    
    
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email',  'phone', 'company_name', 'company_address', 'country',
                'billing_address_line1',  'billing_address_line2', 'city', 'state', 'zip_code', 'shopping_first_name',
                'shopping_last_name', 'shopping_email', 'shopping_phone', 'shopping_company', 
                'shopping_address', 'shopping_address_line1', 'shopping_country', 'shopping_address_line2', 'shopping_city', 
                'shopping_state', 'shopping_zip_code', 'notes')
          
          
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-item input-item-name gs_input_area',
                                                'placeholder': 'First Name:'}),
            'last_name': forms.TextInput(attrs={'class': 'input-item input-item-name gs_input_area',
                                                'placeholder': 'Last Name:'}),
            'email': forms.EmailInput(attrs={'class': 'input-item input-item-email gs_input_area',
                                            'placeholder': 'Email Address:'}),
            'phone': forms.TextInput(attrs={'class': 'input-item input-item-phone gs_input_area',
                                            'placeholder': 'Phone Number:'}), 
            'company_name': forms.TextInput(attrs={'class': 'input-item input-item-website gs_input_area',
                                                'placeholder': 'Company Name (optional):'}),
            'company_address': forms.TextInput(attrs={'class': 'input-item input-item-website gs_input_area',
                                                    'placeholder': 'Company Address (optional):'}),
            'billing_address_line1': forms.TextInput(attrs={'class': 'input-item gs_input_area',
                                                    'placeholder': 'House Number and Street Name:'}),
            'billing_address_line2': forms.TextInput(attrs={'class': 'input-item gs_input_area',
                                                    'placeholder': 'Apartment, unit etc. (optional):'}),
            'city': forms.TextInput(attrs={'class': 'input-item gs_input_area',
                                        'placeholder': 'City:'}),
            'state': forms.TextInput(attrs={'class': 'input-item gs_input_area',
                                            'placeholder':'State:'}),
            'zip_code': forms.TextInput(attrs={'class': 'input-item gs_input_area',
                                                'placeholder': 'Zip Code:'}),
            'shopping_first_name': forms.TextInput(attrs={'class': 'input-item input-item-name gs_input_area',
                                                        'placeholder': 'First Name:'}),
            'shopping_last_name': forms.TextInput(attrs={'class': 'input-item input-item-name gs_input_area',
                                                        'placeholder': 'Last Name:'}),
            'shopping_email': forms.EmailInput(attrs={'class': 'input-item input-item-email gs_input_area',
                                                    'placeholder': 'Email Address:'}),
            'shopping_phone': forms.TextInput(attrs={'class':'input-item input-item-phone gs_input_area',
                                                    'placeholder': 'Phone Number:'}),
            'shopping_company': forms.TextInput(attrs={'class': 'input-item input-item-website gs_input_area',
                                                    'placeholder': 'Company Name (optional):'}),
            'shopping_address': forms.TextInput(attrs={'class': 'input-item input-item-website gs_input_area',
                                                    'placeholder': 'Company Address (optional):'}),
            'shopping_address_line1': forms.TextInput(attrs={'class': 'input-item gs_input_area',
                                                         'placeholder': 'House Number and Street Name:'}),
            'shopping_address_line2': forms.TextInput(attrs={'class': 'input-item gs_input_area',
                                                         'placeholder': 'Apartment, unit etc. (optional):'}),
            'shopping_city': forms.TextInput(attrs={'class': 'input-item gs_input_area',
                                                'placeholder': 'City:'}),
            'shopping_state': forms.TextInput(attrs={'class': 'input-item gs_input_area',
                                                 'placeholder': 'State:'}),
            'shopping_zip_code': forms.TextInput(attrs={'class': 'input-item gs_input_area',
                                                    'placeholder': 'Zip Code:'}),
            'notes': forms.Textarea(attrs={'class': 'input-item input-item-textarea gs_input_area',
                                        'placeholder': 'Notes about your order, e.g. Special notes for Delivery:'})
        }
        
        
#def __init__(self, *args, **kwargs):
            #super().__init__(*args, **kwargs)

#self.fields['shopping_country'].choices = COUNTRIES
#self.fields['country'].choices = COUNTRIES
#'country': forms.Select(attrs={'class': 'input-item gs_input_area'}),
#'shopping_country': forms.Select(attrs={'class': 'input-item gs_input_area w-100'}),