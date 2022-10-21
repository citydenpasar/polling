from django.db import models

# Create your models here.
class Polling(models.Model):
    

    def __str__(self):
        return self.nama
    
    nama = models.CharField(max_length=50)
    tahun = models.IntegerField()