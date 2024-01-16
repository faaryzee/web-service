from django.db import models
from departemens.models import Departemen

# Create your models here.
class Kantor(models.Model):
  title = models.CharField(max_length=255)
  lokasi = models.TextField()
  departemen =  models.ForeignKey(Departemen, on_delete=models.CASCADE, default=1)

  def __str__(self) :
    return self.title