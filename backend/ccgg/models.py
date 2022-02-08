from django.db import models

class CO2_MM_MLO(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    decimal_date = models.DecimalField(max_digits=10, decimal_places=4)
    average = models.DecimalField(max_digits=10, decimal_places=2)
    interpolated = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return str(self.year) + "-" + str(self.month)

    class Meta:
        verbose_name = "CO2 Monthly Mean Mauna Loa Observatory"
        verbose_name_plural = "CO2_MM_MLO"

