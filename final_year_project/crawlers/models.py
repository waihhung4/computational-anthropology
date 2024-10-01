from django.db import models

# Create your models here.

class Url(models.Model):
    source = models.CharField(max_length=100)
    url = models.URLField(max_length = 200)
    search_keyword = models.CharField(max_length=100)

    def __str__(self):
        return self.source
    
class Content(models.Model):
    text = models.TextField()
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
