from django.db import models
from plant_disease.Model.plant import Plante

class Pest(models.Model):
    MALADIE_TYPES = [
        ('insecte', 'Insecte'),
        ('champignon', 'Champignon'),
        ('bacterie', 'Bactérie'),
        ('virus', 'Virus'),
        ('nematode', 'Nématode'),
    ]

    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=MALADIE_TYPES)  # Ajout des choix ici
    description = models.TextField()
    image = models.ImageField(upload_to='images/pests/', blank=True, null=True)
    plantes = models.ManyToManyField(Plante, related_name='pests')

    def __str__(self):
        return self.nom
