from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.




    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    detailedDescription = models.TextField(default='Test Description')
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    score = models.IntegerField(default=0, validators=[ MaxValueValidator(5), MinValueValidator(0)] )
    
    def __str__(self):
        return str(self.pk)
    
    #def averagereview(self):
    #  review = Review.objects.filter(project=self).aggregate(avarage=Avg('score'))
    #  avg=0
    #  if review["avarage"] is not None:
    #      avg=float(review["avarage"])
    #  return avg

    
