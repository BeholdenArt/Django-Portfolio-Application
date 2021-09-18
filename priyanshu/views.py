from django.conf import settings
from django.http.response import HttpResponseServerError
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Home, About, Profile, Category, Resume, Portfolio, Contact, Resume
from django.http import HttpResponse
import os
# Create your views here.


def index(request):

    # Home
    home = Home.objects.latest('updated')
    print(home)
    # About & Socials
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    # Contact me
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        contact.name = name
        contact.email = email
        contact.content = content
        contact.save()
        return redirect('/')

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
    }

    return render(request, 'index.html', context)


def downloadRESUME(request):
    resume = Resume.objects.latest('updated')
    with open(os.path.join(settings.MEDIA_ROOT, 'myResume.pdf'), "rb") as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename= myResume.pdf'
        return response
