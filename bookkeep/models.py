from django.db import models


# Create your models here.
class AccTree(models.Model):
    ID = models.AutoField(primary_key=True, blank=True)
    pID = models.IntegerField(null=True)
    Name = models.CharField(max_length=50)

    def insert(self):
        self.save()
