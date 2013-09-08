# Create your views here.
#-*- coding: UTF-8 -*-
from press.models import Press,Tag,Category
from django.shortcuts import render_to_response
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

def PageView(request,p,template_name):         #分页函数
    page_size = 10
    after_range_num = 5
    before_range_num = 4
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(p,page_size)      #分页对象
    try:
        pressList = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        pressList = paginator.page(1)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+before_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+before_range_num]
    return render_to_response(template_name,{"p":p,"pressList":pressList,
                                           "page_range":page_range,})

def HomeView(request):
    homePress = Press.objects.all()
    template_name = 'home.html'
    return PageView(request,homePress,template_name)

def TagView(request,id):
    cate_name = Category.objects.get(id=id)
    atricles = Press.objects.filter(category=cate_name)
    return render_to_response("category.html",{"articles":atricles,"cate_name":cate_name})
    
def CategoryView(request):
    if request.GET:
        cid = int(request.GET['c'])
    else:
        cid = None
    category = Category.objects.all()
    return render_to_response("category.html",{"category":category,"cid":cid})

def ArticleView(request,id):
    next = request.path
    article = Press.objects.get(id=id)
    return render_to_response("article.html",{"article":article,"next":next},context_instance=RequestContext(request))

def ArchiveView(request):
    archivePress = Press.objects.all()
    return render_to_response('archive.html',{"presses":archivePress})
    