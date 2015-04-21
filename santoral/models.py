from django.db import models

class Santo(models.Model):
    santo = models.CharField(max_length=50)
    fecha = models.DateField()
