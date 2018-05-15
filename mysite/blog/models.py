from django.db import models

# Create your models here.

#think of it like your entire database, each class is a table, each variable
#is a column
#attributes --> metadata

class Post(models.Model):
    title = models.CharField(max_length=140)     #shorter
    body = models.TextField()
    date = models.DateTimeField()

    #metadata purposes
    def __str__(self):
        return self.title

    
