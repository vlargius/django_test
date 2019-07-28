from django.db import models


class Mark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    note = models.CharField(max_length=255)

    def __str__(self):
        return note

# Create your models here.
