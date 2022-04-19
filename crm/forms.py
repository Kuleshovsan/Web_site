from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, label='имя', widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=200, label='телефон', widget=forms.TextInput(attrs={'class':'form-control'}))