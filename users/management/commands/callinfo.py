import os
from datetime import datetime

from django.core.management import BaseCommand

from config import settings
from organization.models import Organization
from users.models import User
from event.models import Event


class Command(BaseCommand):

    def handle(self, *args, **options):
        pass
        # for el in range(2, 6):
        #     organization = Organization.objects.create(
        #         title=f"test{el}",
        #         description=",kf ,kf ,kf",
        #         address=f"street{el}",
        #         postcode=f"0{str(el)*5}",
        #     )
        #     organization.save()

        # for el in range(2, 5):
        #     user = User.objects.create(
        #         email=f"test{el}@example.com",
        #         is_staff=False,
        #         is_superuser=False,
        #         organization=Organization.objects.get(pk=el)
        #
        #     )
        #     user.set_password(str(el)*10)
        #     user.save()
        # for el in range(1, 4):
        #     event = Event.objects.create(
        #         title='Event ' + str(el),
        #         description='бла бла бла',
        #         image="static/images/Screenshot_from_2024-03-11_16-13-05.png",
        #         date=datetime.now()
        #     )
        #     event.organization.set([Organization.objects.get(pk=el)])
        #     event.save()

