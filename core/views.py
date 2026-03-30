from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReservationForm, ContactForm
from .models import Reservation, ContactMessage

# Create your views here.
def home(request):
  dishes = [
    {
      'name': 'Paneer Butter Masala',
      'desc': 'Creamy and rich, with a delightful blend of spices, perfect with naan or rice.',
      'image': 'core/images/butterpaneer.jpg'
    },
    {
      'name': 'Salmon Fish Curry',
      'desc': 'Succulent salmon in creamy, spiced curry with a perfect balance of flavors.',
      'image': 'core/images/salmonfishcurry.jpg'
    },
    {
      'name': 'Butter Chicken',
      'desc': 'A royal dish with a creamy, nutty gravy that offers a rich, unforgettable taste.',
      'image': 'core/images/butterchicken.jpg'
    }
        ]
  
  return render(request, "core/home.html", {'dishes': dishes})



def menu(request):
  return render(request, "core/menu.html") 



def tracking(request):
  return render(request, "core/tracking.html")


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "🎉 Your table has been reserved! We'll see you soon.")
            return redirect('reservation')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ReservationForm()

    return render(request, 'core/reservation.html', {'form': form})



def contact(request):
  if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
            )
            messages.success(request, "✅ Your message has been sent! We'll get back to you soon.")
            return redirect('contact')
        else:
            messages.error(request, "Please fix the errors below.")
  else:
    form = ContactForm()

  return render(request, 'core/contact.html', {'form': form})