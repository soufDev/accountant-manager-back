from django.db import models

# Create your models here.


class Contract(models.Model):
    file = models.FileField(upload_to="files/")

    def __str__(self):
        return self.file