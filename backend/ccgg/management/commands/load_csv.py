
import csv
from django.core.management import BaseCommand
from ccgg.models import CO2_MM_MLO

class Command(BaseCommand):
    help = "Load data from CSV file"

    def handle(self, *args, **options):
        file_path = "ccgg/management/commands/co2_mm_mlo.csv"
        with open(file_path, "r") as csv_file:
            csv_data = csv.reader(csv_file, dialect=csv.excel)
            for row in csv_data:
                # Skip comments and first row
                if row[0].startswith("#"):
                    continue
                if row[0] == "year":
                    continue
                CO2_MM_MLO.objects.create(
                    year = row[0],
                    month = row[1],
                    decimal_date = row[2],
                    average = row[3],
                    interpolated = row[4]
                )
