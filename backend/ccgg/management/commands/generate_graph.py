import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from django.core.management import BaseCommand
from ccgg.models import CO2_MM_MLO


class Command(BaseCommand):
    help = "Generate Matplot graph"

    def handle(self, *args, **options):
        decimal_date = []
        average = []
        interpolated = []
        for row in CO2_MM_MLO.objects.all():
            decimal_date.append(row.decimal_date)
            average.append(row.average)
            interpolated.append(row.interpolated)

        fig, ax = plt.subplots()
        ax.plot(decimal_date, average)
        ax.plot(decimal_date, interpolated)
        ax.tick_params(direction='in', which='both')
        ax.set_xlabel('Year')
        ax.set_ylabel('parts per million (ppm)')
        ax.yaxis.set_major_locator(MultipleLocator(20))
        ax.yaxis.set_minor_locator(MultipleLocator(10))
        ax.xaxis.set_major_locator(MultipleLocator(10))
        ax.xaxis.set_minor_locator(MultipleLocator(5))
        ax.set_title('Atmospheric CO_2 at Mauna Loa Observatory')
        plt.savefig("ccgg/static/ccgg/co2_mm_mlo_full_record.png")

        ax.set_title('Recent monthly mean CO_2 at Mauna Loa Observatory')
        ax.set_xlim(2016, 2022)
        ax.set_ylim(399, 421)
        ax.yaxis.set_major_locator(MultipleLocator(5))
        ax.yaxis.set_minor_locator(MultipleLocator(1))
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_minor_locator(MultipleLocator(0.2))
        plt.savefig("ccgg/static/ccgg/co2_mm_mlo_recent.png")






