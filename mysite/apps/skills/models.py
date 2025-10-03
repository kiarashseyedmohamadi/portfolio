from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Skill(models.Model):
    name = models.CharField(max_length=50) 
    rating = models.PositiveSmallIntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return f"{self.name} ({self.rating} ⭐)"

