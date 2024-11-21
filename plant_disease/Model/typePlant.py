from django.db import models


class TypePlante(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/plantes/', blank=True, null=True)

    def __str__(self):
        return self.nom

