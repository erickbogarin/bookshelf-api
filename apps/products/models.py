from django.db import models
from django.template.defaultfilters import slugify

# Product Category


class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(db_index=True, unique=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title