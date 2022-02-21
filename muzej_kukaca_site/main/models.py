from django.db import models
from django.conf import settings

class Kukac(models.Model):
    vrsta = models.CharField(max_length = 100)
    porodica = models.CharField(max_length = 100)
    red = models.CharField(max_length = 100)
    lokalitet = models.CharField(max_length = 100)
    duljina = models.CharField(max_length = 20)
    spol = models.CharField(max_length = 1)
    opis = models.TextField()
    lovac = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slika = models.ImageField(upload_to = 'images/')
    datum_sakupljanja = models.DateTimeField(blank=True, null=True)    

    def __str__(self):
        return self.vrsta