from django.db import models
from plant_disease.Model.plant import Plante  # Assurez-vous que ce chemin est correct
from plant_disease.Model.maladie import Maladie  # Assurez-vous que ce chemin est correct
from plant_disease.Model.traitement import Traitement  # Assurez-vous que ce chemin est correct

class Diagnostic(models.Model):
    plante = models.ForeignKey(Plante, on_delete=models.CASCADE, related_name='diagnostics')  # Plante concernée par le diagnostic
    maladie = models.ForeignKey(Maladie, on_delete=models.CASCADE, related_name='diagnostics')  # Maladie identifiée
    traitement = models.ForeignKey(
        Traitement,
        on_delete=models.SET_NULL,  # Si un traitement est supprimé, le champ devient nul
        related_name='diagnostics',
        null=True,
        blank=True
    )  # Traitement recommandé (facultatif)
    date_diagnostic = models.DateField(auto_now_add=True)  # Date du diagnostic
    notes = models.TextField(blank=True, null=True)  # Notes supplémentaires

    def __str__(self):
        return f"Diagnostic de {self.maladie.nom} pour {self.plante.nom} le {self.date_diagnostic}"
