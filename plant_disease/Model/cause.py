# models.py (for CauseMaladie)
from django.db import models
from plant_disease.Model.maladie import Maladie  # Ensure this import is correct

class CauseMaladie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100)

    # ForeignKey to Maladie with a unique related_name
    maladie = models.ForeignKey(Maladie, on_delete=models.CASCADE, related_name='cause_maladies', null=True)  
    
    def __str__(self):
        return self.nom
