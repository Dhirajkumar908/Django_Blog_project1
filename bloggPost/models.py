from django.db import models

# Create your models here.


class blogg(models.Model):
    bloggtitle = models.CharField(max_length=100)
    bloggContent = models.TextField()

    def __str__(self):
        return self.bloggtitle
