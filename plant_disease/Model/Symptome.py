from django.db import models
from plant_disease.Model.plant import Plante 
class Symptome(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    plante = models.ForeignKey(Plante, on_delete=models.CASCADE, related_name='symptomes', null=True)  # New foreign key to Plante

    def __str__(self):
        return self.nom