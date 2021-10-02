from django.views.generic import TemplateView, FormView

from .models import HomePage, AboutPage
from Gallery.models import Photo
from .forms import ContactForm

import random


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        model_data_list = HomePage.objects.all()

        if not model_data_list:
            return context

        context["data"] = model_data_list[0]

        # todo change this to a random image from database
        frontpage_photo_list = Photo.objects.filter(frontpage=True)
        if frontpage_photo_list:
            context["photo"] = random.choice(frontpage_photo_list)

        return context


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        about_data_list = AboutPage.objects.all()
        if not about_data_list:
            return context

        context["data"] = about_data_list[0]
        
        return context