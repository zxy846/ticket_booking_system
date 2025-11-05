from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        widgets = {
            'seat_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g.: 12A'
            }),
            'booking_reference': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g.: ABC123'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'flight': forms.Select(attrs={
                'class': 'form-control'
            }),
            'passenger': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 为所有字段添加英语标签
        self.fields['flight'].label = 'Flight'
        self.fields['passenger'].label = 'Passenger'
        self.fields['seat_number'].label = 'Seat Number'
        self.fields['booking_reference'].label = 'Booking Reference'
        self.fields['price'].label = 'Price'
        self.fields['status'].label = 'Status'