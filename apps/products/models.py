from django.db import models
from django.template.defaultfilters import slugify

from apps.bookshelf.models import TimestampedModel


class Book(TimestampedModel):
    title = models.CharField(max_length=120)
    slug = models.SlugField(db_index=True, max_length=255, unique=True)

    image = models.URLField(blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    isbn = models.CharField(max_length=100)
    date_published = models.DateField()
    pages = models.IntegerField()

    categories = models.ManyToManyField(
        'Category', related_name='books',
    )

    author = models.ForeignKey(
        'profiles.Author',
        related_name='books',
        on_delete=models.CASCADE
    )

    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


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