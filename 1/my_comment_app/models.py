from django.db import models
from django import forms
from django.contrib.comments.models import Comment
# Create your models here.

class CommentWithReply(Comment):
    rName = models.CharField("rName",max_length=20)
    rContent = models.TextField("rContent")
