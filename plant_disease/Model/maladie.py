# models.py (for Maladie)
from django.db import models
from plant_disease.Model.plant import Plante  # Ensure this import is correct

class Maladie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(
        max_length=50,
        choices=[
            ('bactérienne', 'Bactérienne'),
            ('fongique', 'Fongique'),
            ('virale', 'Virale'),
        ]
    )
    plantes = models.ManyToManyField(Plante, related_name='maladies')

    def __str__(self):
        return self.nom
