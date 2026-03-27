from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, "core/home.html")

def menu(request):
  return render(request, "core/menu.html") 

def tracking(request):
  return render(request, "core/tracking.html")

def reservation(request):
  return render(request, "core/reservation.html")

def contact(request):
  return render(request, "core/contact.html")