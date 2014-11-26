from django.db import models

# Create your models here.

class Page(models.Model):
    page_name = models.CharField(max_length=60, unique=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.page_name


class Post(models.Model):
    page = models.ForeignKey(Page)
    title = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.URLField()
    pub_date = models.DateTimeField('date published', auto_now=True)
    layout= models.CharField(max_length=50, default="one")
    order = models.IntegerField(default=0)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.title