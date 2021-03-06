from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length = 100)
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

