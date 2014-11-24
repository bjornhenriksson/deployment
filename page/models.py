from django.db import models

# Create your models here.

class Page(models.Model):
    page_name = models.CharField(max_length=60, unique=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.page_name


class Post(models.Model):
    page = models.ForeignKey(Page)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    picture = models.URLField()
    pub_date = models.DateTimeField('date published')
    order = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.title