from django.db import models
from plant_disease.Model.Symptome import  Symptome
class prevention(models.Model):
    """Modèle représentant les mesures préventives pour les maladies des plantes."""
    nom = models.CharField(max_length=100)
    description = models.TextField()
    symptômes_connexes = models.ForeignKey(Symptome, on_delete=models.CASCADE, related_name='mesures_préventives')

    def __str__(self):
        return self.nom