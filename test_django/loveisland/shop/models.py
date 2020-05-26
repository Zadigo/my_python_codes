from django.db import models

# Create your models here.

class Boutique(models.Model):
    name = models.CharField(max_length=165)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name