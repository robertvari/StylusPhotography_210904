from django.db import models


class PageInfo(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)

    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Oldal infó"

    def __str__(self):
        return f"{self.title}: {self.subtitle}"


class HomePage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    content = models.TextField(max_length=2000, blank=True)

    class Meta:
        verbose_name_plural = "Home page infó"

    def __str__(self):
        return self.title


class AboutPage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    content = models.TextField(max_length=2000, blank=True)

    class Meta:
        verbose_name_plural = "About page infó"

    def __str__(self):
        return self.title