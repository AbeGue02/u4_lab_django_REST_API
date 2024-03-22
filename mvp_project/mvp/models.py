from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    wins = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    losses = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self) -> str:
        return self.name
    
class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='songs')
    position = models.CharField(max_length=100)
    age = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    is_injured = models.BooleanField()

    def __str__(self) -> str:
        return self.name