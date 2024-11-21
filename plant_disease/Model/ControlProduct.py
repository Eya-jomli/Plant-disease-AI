from django.db import models
from plant_disease.Model.pest import Pest  # Assurez-vous que l'importation est correcte selon l'organisation de votre projet

class ControlProduct(models.Model):
    PRODUCT_TYPES = [
        ('insecticide', 'Insecticide'),
        ('acaricide', 'Acaricide'),
        ('fongicide', 'Fongicide'),
        ('bactériostatique', 'Bactériostatique'),
        ('nématicide', 'Nématicide'),
    ]

    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    description = models.TextField()
    méthode_application = models.CharField(max_length=100, help_text="Méthode d'application du produit (ex: pulvérisation)")
    efficacité = models.DecimalField(max_digits=5, decimal_places=2, help_text="Efficacité en pourcentage")
    pests = models.ManyToManyField(Pest, related_name='control_products')

    def __str__(self):
        return self.nom
