import random
from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Kukac
from main.factory import (
    KukacFactory
)

NUM_KUKACS= 10

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Kukac]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_KUKACS):
            kukac = KukacFactory()
