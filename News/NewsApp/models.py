from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    author = models.models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.content} {self.status} {self.author},{self.created_at}'
    
