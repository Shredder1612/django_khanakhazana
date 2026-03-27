from django.shortcuts import render

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
  return render(request, "core/reservation.html")



def contact(request):
  return render(request, "core/contact.html")