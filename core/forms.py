from django import forms
from .models import Reservation
import datetime

class ReservationForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'min': datetime.date.today().isoformat(),
                'class': 'w-full border border-orange-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400 bg-white'
            }
        )
    )

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests', 'special_requests']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your full name',
                'class': 'w-full border border-orange-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com',
                'class': 'w-full border border-orange-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+91 98765 43210',
                'class': 'w-full border border-orange-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400'
            }),
            'time': forms.Select(attrs={
                'class': 'w-full border border-orange-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400 bg-white'
            }),
            'guests': forms.NumberInput(attrs={
                'placeholder': '2',
                'min': '1',
                'max': '20',
                'class': 'w-full border border-orange-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400'
            }),
            'special_requests': forms.Textarea(attrs={
                'placeholder': 'Birthday celebration, window seat, allergies...',
                'rows': 3,
                'class': 'w-full border border-orange-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400'
            }),
        }