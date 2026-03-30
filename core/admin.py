from django.contrib import admin
from .models import Reservation, ContactMessage

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'time', 'guests', 'phone', 'created_at']
    list_filter = ['date', 'time']
    search_fields = ['name', 'email', 'phone']
    ordering = ['date', 'time']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['subject', 'is_read']
    search_fields = ['name', 'email']
    ordering = ['-created_at']
    list_editable = ['is_read']     