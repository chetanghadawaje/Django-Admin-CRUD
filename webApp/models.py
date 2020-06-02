from django.db import models
from django.core.validators import FileExtensionValidator


class category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class tag(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.name


class product(models.Model):
    category = models.ForeignKey(category, models.DO_NOTHING)
    tag = models.ForeignKey(tag, models.DO_NOTHING)
    name = models.CharField(max_length=25, blank=False, null=False)
    image = models.FileField(upload_to='static/image/', blank=False, null=False)
    description = models.TextField(max_length=100, blank=False, null=False)