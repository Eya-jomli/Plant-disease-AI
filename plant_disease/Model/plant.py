from django.db import models
from plant_disease.Model.typePlant import TypePlante

class Plante(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/plantes/', blank=True, null=True)
    type_plante = models.ForeignKey(TypePlante, on_delete=models.CASCADE, related_name='plantes')

    def __str__(self):
        return self.nom