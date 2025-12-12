from django import forms
from .models import Passenger

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['first_name', 'last_name', 'date_of_birth', 'passport_number', 'email', 'phone']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'first_name': '名',
            'last_name': '姓',
            'date_of_birth': '出生日期',
            'passport_number': '护照号码',
            'email': '邮箱',
            'phone': '手机号码',
        }