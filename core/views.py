from django.shortcuts import render




def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def furnitures(request):
    return render(request, "furnitures.html")

def index(request):
    return render(request, "index.html")

def testimonial(request):
    return render(request, "testimonial.html")

