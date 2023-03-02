from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    date = models.DateField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
