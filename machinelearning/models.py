from django.db import models

class CarTerrain(models.Model):
    bumpy = models.FloatField(max_length=10)
    grade = models.FloatField(max_length=10)
    speed = models.CharField(max_length=10)

    def __str__(self):
        return self.speed


class Algorithm(models.Model):
    algo_code = models.CharField(max_length=10)
    algo_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.algo_name