from django.shortcuts import render
from .models import Farmer
# In views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Sericulture Management!")

def add_farmer(request):
    return render(request, 'farmer_form.html')

def market_trends(request):
    return render(request, 'market_trends.html') 

def home(request):
    return render(request, 'home.html') 

def contact(request):
    return render(request, 'contact.html')

def add_farmer(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        # Save the farmer data into the database
        Farmer.objects.create(name=name, contact=contact)
        return render(request, 'success.html')  # Correctly render success page
    return render(request, 'farmer_form.html')  # Render form page
