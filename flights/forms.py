from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'
        widgets = {
            'flight_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g.: AA123'
            }),
            'departure_airport': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g.: JFK'
            }),
            'arrival_airport': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g.: LAX'
            }),
            'departure_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
            'arrival_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
            'total_seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
            'available_seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 为所有字段添加英语标签
        self.fields['flight_number'].label = 'Flight Number'
        self.fields['departure_airport'].label = 'Departure Airport'
        self.fields['arrival_airport'].label = 'Arrival Airport'
        self.fields['departure_time'].label = 'Departure Time'
        self.fields['arrival_time'].label = 'Arrival Time'
        self.fields['total_seats'].label = 'Total Seats'
        self.fields['available_seats'].label = 'Available Seats'