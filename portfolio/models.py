from django.db import models
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

#Create Portfolio
class Portfolio(models.Model):
    title = models.CharField(max_length=10, unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, help_text="The date and time this page was created. Automatically generated when the model saves.")
    picture = models.ImageField(upload_to='portfolios/covers/',)
    slug = models.CharField(max_length=10, blank=True, editable=False,
                            help_text="Unique URL path to access this page. Generated by the system.")
    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
