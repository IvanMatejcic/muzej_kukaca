from django.db import models

class Korisnik(models.Model):
    username = models.CharField(max_length = 11)
    ime = models.CharField(max_length = 20)
    prezime = models.CharField(max_length = 20)
    email = models.EmailField()
    slika_profila = models.ImageField(upload_to = 'images/', default = '0')

    def __str__(self):
        return self.username


class Kukac(models.Model):
    vrsta = models.CharField(max_length = 100)
    porodica = models.CharField(max_length = 100)
    red = models.CharField(max_length = 100)
    datum_sakupljanja = models.DateField()
    lokalitet = models.CharField(max_length = 100)
    duljina = models.CharField(max_length = 20)
    spol = models.CharField(max_length = 1)
    dostupan = models.BooleanField(default = False)
    opis = models.TextField()
    lovac = models.ForeignKey(Korisnik, on_delete = models.CASCADE)
    slika = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.vrsta