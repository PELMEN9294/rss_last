from django.db import models
import datetime
# Create your models here.

class News(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.TextField(max_length=50)
    text = models.TextField()
    date = models.DateField(default=str(datetime.datetime.now())[:10])

    def __str__(self):
        return str(self.id) + "_" + str(self.title)
