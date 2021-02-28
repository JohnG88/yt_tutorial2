from django.db import models

# Create your models here.

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    # When you see the name Search in admin it will look like Searchs this line makes it look like Searches
    class Meta:
        verbose_name_plural = 'Searches'

    def __str__(self):
        return self.search
