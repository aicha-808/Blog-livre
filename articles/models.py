from django.conf import settings
from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=100)
    resume = models.CharField(max_length=300)
    contenu = models.TextField(blank=True)
    date_publication = models.DateField(auto_now_add=True)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)
    lien_pdf = models.URLField(max_length=500, blank=True, null=True)
    audio = models.URLField(max_length=500, blank=True, null=True, help_text="Lien du livre audio")
    

    def __str__(self):
        return self.titre
