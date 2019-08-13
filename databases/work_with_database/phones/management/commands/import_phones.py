import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from slugify import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                new_phone = Phone.objects.create(
                    name=line[1],
                    image=line[2],
                    price=line[3],
                    release_date=line[4],
                    lte_exists=line[5],
                    slug=slugify(line[1])
                )
                print(new_phone)
