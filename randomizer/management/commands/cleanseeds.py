from datetime import timedelta

from django.core.management.base import BaseCommand, CommandParser
from django.db import transaction
from django.utils import timezone

from randomizer.models import Seed


class Command(BaseCommand):
    help = 'Remove old seeds that are from previous versions, or at least 6 months old.'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            '--age',
            type=lambda x: timedelta(days=int(x)),
            default=timedelta(days=7),
            help="Minimum age in days for seeds to remove.  Default: %(default)s",
        )

    def handle(self, *args, **options):
        count = 0
        min_age = timezone.now() - options['age']

        for seed in Seed.objects.filter(generated__lte=min_age):
            with transaction.atomic():
                seed.patch_set.all().delete()
                seed.delete()
                count += 1

        self.stdout.write("Cleared {} old seeds".format(count))
