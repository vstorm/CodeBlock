from django.db import models

# Create your models here.

class Category(models.Model):
    cname = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.cname

class Tag(models.Model):
    tname = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.tname

class Press(models.Model):
    title = models.CharField(max_length=50)
    title_en = models.CharField(max_length=100)
    cover = models.CharField(max_length=200)
    date_pub = models.DateTimeField(auto_now=True)
    page_view = models.IntegerField(default=0)
    introduce = models.TextField()
    content = models.TextField()
    
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)
    
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ["-date_pub"]

# class CommentWithReply(models.Model):

