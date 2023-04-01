from django.shortcuts import render
from django.views import View
from .models import AboutMe, Ability, WhatIOffer, App, Contact, PDFUpload
from .forms import ContactForm

class AboutMeView(View):
    def get(self, request):
        form = ContactForm()
        query_set = AboutMe.objects.last()
        ability = Ability.objects.all()
        my_offers = WhatIOffer.objects.all()
        my_works = App.objects.all()
        pdf = PDFUpload.objects.last()
        return render(
            request,
            'base/home.html',
            context={'owner': query_set,
                     'ability': ability,
                     'my_offers': my_offers,
                     'my_works': my_works,
                     'form': form,
                     'pdf': pdf,
                     }
        )

    def post(self, reqeust):
        form_data = ContactForm(data=reqeust.POST)
        if form_data.is_valid():
            cd = form_data.cleaned_data
            print(cd, 40 * '*')
            contact = Contact.objects.create(name=cd['name'], email=cd['email'], text=cd['text'])
            contact.save()
            return render(reqeust, 'base/home.html')
        return render(reqeust, 'base/home.html')
