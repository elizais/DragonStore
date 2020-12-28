from django import forms


class BuyerForm(forms.Form):
    name = forms.CharField(label='Name', required=True, help_text='Enter your name')
    last_name = forms.CharField(label='Last Name', required=True, help_text='Enter your last name')
    cellphon = forms.CharField(label='Cellphone', required=True, help_text='Enter your phone number')
    email = forms.EmailField(label='Email', required=True, help_text='Enter your phone number')




