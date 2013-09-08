#-*- coding: UTF-8 -*-
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from press.models import Press

class LatestPress(Feed):
    title = "Feed订阅 |CodeBlock"
    link = "/archive/"
    description = "最新5篇文章"
    
    def items(self):
        return Press.objects.order_by("-date_pub")[:5]
    
    def item_link(self,item):
        return reverse('article',args=[item.id])
    
    def item_tile(self,item):
        return item.title
    
    def item_description(self,item):
        return item.content
    