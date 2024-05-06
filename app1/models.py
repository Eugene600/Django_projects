from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    def snippet(self):
        return self.body[:50] + "...."    
    