from django.db import models

# Create your models here.

class PrimarySchool(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    district_name = models.CharField(max_length=50)
    medium = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return str(self.id) + "," + self.district_name + "," + self.medium + "," + self.category
    
'''
from school.models import PrimarySchool
import csv
with open('data/primaryschool.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        entry = PrimarySchool(id=row['id'], district_name=row['district_name'], medium=row['moi'], category=row['cat'])
        entry.save()
        
'''
