from django.db import models
import uuid

# Create your models here.

class Book(models.Model):
    id   = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    url  = models.URLField(max_length=255)
    is_downloaded = models.BooleanField(default= False)
    downloaded_file = models.FileField(upload_to ='uploads/',blank=True, null=True) 


    def __str__(self):
        return self.name

        