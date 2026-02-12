## exmaple model for artifact, placeholder for osamas worl

from django.db import models
class Artefact(models.Model):
    ##for not i will only do title, again this is a placeholder for osama
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_archived = models.BooleanField(default=False)
    ##to create uplod field for the database
    file = models.FileField(upload_to='artefacts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
