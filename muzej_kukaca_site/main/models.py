from django.db import models
from django.conf import settings



class Kukac(models.Model):
    vrsta = models.CharField(max_length = 100)
    porodica = models.CharField(max_length = 100)
    red = models.CharField(max_length = 100)
    spol = models.CharField(max_length = 1)
    duljina = models.CharField(max_length = 2)
    lokalitet = models.CharField(max_length = 100)
    datum_sakupljanja = models.DateTimeField(blank=True, null=True)    
    opis = models.TextField()
    slika = models.ImageField(upload_to = 'images/')
    lovac = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = '0')

    GENDER_MALE = 'M'
    GENDER_FEMALE = 'Ž'
    
    def __str__(self, spol=None):
        self.spol = spol
        return self.vrsta