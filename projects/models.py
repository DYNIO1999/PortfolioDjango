from unittest import result
from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.




    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    detailedDescription = models.TextField(default='Test Description')
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    score = models.IntegerField(default=0)
    counter = models.IntegerField(default=0)
    avg =  models.FloatField(default=0.0)
    
    def __str__(self):
        return str(self.pk)
    
    def updateScore(self, value):
        self.score = self.score+value
        self.counter = self.counter+1
    
    def averagereview(self):
        result = self.score/self.counter
        return result
    
