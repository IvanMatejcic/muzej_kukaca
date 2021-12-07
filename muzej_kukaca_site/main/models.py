from django.db import models

class Korisnik(models.Model):
    korisnik_username = models.CharField(max_length = 11)
    korisnik_ime = models.CharField(max_length = 20)
    korisnik_prezime = models.CharField(max_length = 20)
    korisnik_email = models.EmailField()

    def __str__(self):
        return self.korisnik_username


class Kukac(models.Model):
    kukac_vrsta = models.CharField(max_length = 100)
    kukac_porodica = models.CharField(max_length = 100)
    kukac_red = models.CharField(max_length = 100)
    kukac_datum_sakupljanja = models.DateField()
    kukac_lokalitet = models.CharField(max_length = 100)
    kukac_duljina = models.CharField(max_length = 20)
    kukac_spol = models.CharField(max_length = 1)
    kukac_dostupan = models.BooleanField(default = False)
    kukac_opis = models.TextField()
    kukac_lovac = models.ForeignKey(Korisnik, on_delete = models.CASCADE)

    def __str__(self):
        return self.kukac_vrsta