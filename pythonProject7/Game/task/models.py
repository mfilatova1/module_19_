from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(decimal_places=2, max_digits=100)
    size = models.DecimalField(decimal_places=2, max_digits=100)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)


    def __str__(self):
        return self.title