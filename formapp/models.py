from django.db import models

# Create your models here.
class Emp(models.Model):
    company=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    id=models.IntegerField(primary_key=True)
    designation=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)


    def __str__(self):
        return self.name


