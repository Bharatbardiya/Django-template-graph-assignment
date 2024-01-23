from django.db import models

# Create your models here.

class Match(models.Model):
    season = models.CharField(max_length=255)
    winner = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.season + "," + self.winner
    
    

'''
from matches.models import Match
import csv
with open('data/matches.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        entry = Match(season=row['season'], winner=row['winner'])
        entry.save()
        
'''

    

