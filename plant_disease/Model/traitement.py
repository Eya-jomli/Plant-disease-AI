from django.db import models
from plant_disease.Model.maladie import Maladie  # Ensure the import path is correct

class Traitement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    méthode = models.TextField()
    maladie = models.OneToOneField(
        Maladie,
        on_delete=models.CASCADE,
        related_name='traitement',
        null=True,  # Optional if some treatments aren't linked to diseases
        blank=True  # Optional field in formss
    )

    def __str__(self):
        return self.nom
