from django.db import models
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    date_published = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)  # Add a slug field

    def save(self, *args, **kwargs):
        # Generate the slug from the title
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
        
    def snippet(self):
        return self.body[:50] + "...."
