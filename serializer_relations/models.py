from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    
    def __str__(self): 
        return self.name
    
class Song(models.Model):  
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='songs')

    def formatted_duration(self):
        return f'{self.duration} mins'
    
    def __str__(self): 
        return self.title