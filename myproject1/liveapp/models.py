from django.db import models

class LiveSession(models.Model):
    type = models.CharField(max_length=50)
    unique_id = models.CharField(max_length=100, unique=True)
    userurl = models.URLField(max_length=255)

    def __str__(self):
        return self.unique_id
