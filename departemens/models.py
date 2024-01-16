from django.db import models

class Departemen(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name