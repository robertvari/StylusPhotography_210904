from django.views.generic import TemplateView, DetailView

from .models import Category, Photo


class GalleryView(TemplateView):
    template_name = "gallery.html"

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context["photos"] = Photo.objects.all()
        context["categories"] = Category.objects.all()
        return context


class PhotoDetailView(DetailView):
    template_name = "photo_details.html"
    model = Photo
    context_object_name = "photo"