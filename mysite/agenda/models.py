from django.db import models

class Activiteit(models.Model):
    datum = models.DateField()
    begintijd = models.TimeField()
    eindtijd = models.TimeField()
    omschrijving = models.TextField()
    kosten = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.datum} - {self.omschrijving}'

    class Meta:
        verbose_name_plural = "Activiteiten"