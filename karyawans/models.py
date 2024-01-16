from django.db import models
from kantors.models import Kantor

# Create your models here.
class Review(models.Model):
  kantor = models.ForeignKey(Kantor, related_name='karyawans', on_delete=models.CASCADE)
  # kantor = models.ForeignKey(Kantor, related_name='karyawans', on_delete=models.CASCADE)
  nama = models.CharField(max_length=50)
  jabatan = models.CharField(max_length=100)

  def __str__(self):
    # return self.nama
    return f"Review for {self.kantor.title}"