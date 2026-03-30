from django import forms
from .models import Reservation, ContactMessage
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



class ContactForm(forms.Form):
    SUBJECT_CHOICES = [
        ('', 'Select a subject'),
        ('feedback', 'Feedback'),
        ('complaint', 'Complaint'),
        ('query', 'General Query'),
        ('order', 'Order Issue'),
        ('other', 'Other'),
    ]

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your full name',
            'class': 'w-full border border-orange-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'your@email.com',
            'class': 'w-full border border-orange-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400'
        })
    )

    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full border border-orange-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400 bg-white'
        })
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your message here...',
            'rows': 5,
            'class': 'w-full border border-orange-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400'
        })
    )

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if not subject:
            raise forms.ValidationError("Please select a subject.")
        return subject