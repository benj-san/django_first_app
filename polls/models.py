from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    category_name = models.TextField(max_length=80)

    def __str__(self):
        return self.category_name


class Protagonist(models.Model):
    protagonist_name = models.CharField(max_length=80)
    protagonist_description = models.CharField(max_length=80)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def publish(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s' % (self.protagonist_name, self.protagonist_description)
