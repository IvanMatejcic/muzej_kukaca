import factory
from factory.django import DjangoModelFactory
from main.models import *

# za mogućnost korištenja ImageField-a u factory-boy-u
from django.core.files.base import ContentFile 

# za random biranje user-a za factory-boy
from django.contrib.auth import get_user_model 

class KukacFactory(DjangoModelFactory):
    class Meta:
        model = Kukac

    vrsta = factory.Faker("first_name")
    porodica = factory.Faker("last_name")
    red = factory.Faker("pyint", min_value = 0, max_value = 20)
    spol = factory.Iterator([Kukac.GENDER_MALE, Kukac.GENDER_FEMALE])
    duljina = factory.Faker("pyint", min_value = 1, max_value = 10000)
    lokalitet = factory.Faker("city")
    datum_sakupljanja = factory.Faker("date_time")
    opis = factory.Faker("paragraph")
    lovac = factory.Iterator(get_user_model().objects.all())
    slika = factory.LazyAttribute(
            lambda _: ContentFile(
                factory.django.ImageField()._make_data(
                    {'width': 1024, 'height': 768}
                ), 'example.jpg'
            )
        )