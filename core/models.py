from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=50)
    code_zone = models.CharField(max_length=30)

    def __str__(self):
        return self.name
