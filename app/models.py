from django.db import models

# Create your models here.
class Industry(models.Model):
    industry_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.industry_name




class Actor(models.Model):
    industry_name=models.ForeignKey(Industry,on_delete=models.CASCADE)
    actor_name=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.actor_name




class Movie(models.Model):
    actor_name=models.ForeignKey(Actor,on_delete=models.CASCADE)
    movie_name=models.CharField(max_length=100)
    url=models.URLField()
    def __str__(self):
        return self.movie_name