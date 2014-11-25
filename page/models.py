from django.db import models

# Create your models here.

class Page(models.Model):
    page_name = models.CharField(max_length=60, unique=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.page_name


class Post(models.Model):
    page = models.ForeignKey(Page)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1200)
    picture = models.URLField(default="http://images.puella-magi.net/thumb/2/27/No_Image_Wide.svg/800px-No_Image_Wide.svg.png")
    pub_date = models.DateTimeField('date published')
    layout= models.CharField(max_length=50, default="one")
    order = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.title