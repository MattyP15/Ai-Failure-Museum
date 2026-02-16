from django.db import models

class Exhibit(models.Model):

    title = models.CharField(max_length=200)
    
    #Domain as in flooding, earthquakes etc
    domain = models.CharField(max_length=100)

    #Short summary of the exhibit
    description = models.TextField()
    is_archived = models.BooleanField(default=False)
    
    ##to create upload field for the database
    file = models.FileField(upload_to='exhibits/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
