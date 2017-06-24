#coding:utf-8
from  django.shortcuts import  render_to_response
from django.template.context import RequestContext
from models import  *
def  index(request):
    get_info=request.GET # request.POST
    cateid=get_info.get("cateid")
    if  not cateid:
        article_list = Article.objects.all()[0:11]
    else:
        article_list = Article.objects.filter(cid=int(cateid))[0:11]

    category_list=Category.objects.all()

    return render_to_response("index.html",{"category_list":category_list,'article_list':article_list},
                              context_instance=RequestContext(request))

def detail(request,aid):
    article_list = Article.objects.all()[0:11]
    category_list=Category.objects.all()

    article = Article.objects.get(aid=int(aid))
    return render_to_response('detail.html',{"category_list":category_list,'article_list':article_list,'article':article},
                              context_instance=RequestContext(request))