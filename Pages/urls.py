from django.urls import path

from .views import HomeView, GalleryView, AboutView, ContactView


urlpatterns = [
    path('', HomeView.as_view()),
    path('contact/', ContactView.as_view()),
    path('about/', AboutView.as_view()),
    path('gallery/', GalleryView.as_view())
]