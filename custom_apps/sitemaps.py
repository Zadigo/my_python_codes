from django.contrib.sitemaps import views
from django.contrib.sitemaps import Sitemap

from django.urls import reverse

from offres.models import OffresEntreprise


class HeroSiteMap(Sitemap):
    def items(self):
        return ['hero_entreprise', 'hero_candidats']
    
    def location(self, item):
        return reverse(item)


class OffresEntrepriseSiteMap(Sitemap):
    def items(self):
        return OffresEntreprise.objects.all()

