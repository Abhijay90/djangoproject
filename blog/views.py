# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# from rest_framework.response import Response
from django.http import JsonResponse

from django.views import generic


from .service import *


class initClass(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = User.objects.all().order_by('-date_joined')
    def get(self,request):
        print "why"
        return JsonResponse({'some': 'data'})

    def post(self,request):
        print "why not"
        return JsonResponse({'some': 'data'})



class AddBlog(APIView):
    def post(self,request):
        data = request.data
        title = data["title"]
        content = data["content"]
        if title and content:
            s =BlogArticleBase()
            resp = s.addBlog(title,content)
            # print "all done"
            # print resp
            return JsonResponse(dict(status = True,title = title,content=content))
        return JsonResponse(dict(status = False,title = title,content=content))


class ViewBlog(APIView):
    def get(self,request,blog_id):
        if blog_id:
            s =BlogArticleBase()
            return JsonResponse(s.viewBlog(blog_id))            
        return JsonResponse(dict(status = False))


class ViewBlogList(APIView):
    def get(self,request):
        s =BlogArticleBase()
        return JsonResponse(s.viewBlogList())


class comment(APIView):
    def get(self,request,paragraph_id):
        s =BlogCommentBase()
        return JsonResponse(s.viewComment(paragraph_id))

    def post(self,request,paragraph_id):
        data = request.data
        paragraph_id = data["paragraph_id"]
        content = data["content"]
        s =BlogCommentBase()
        return JsonResponse(s.addComment(paragraph_id,content))



@api_view(['GET'])
def homepage(request):
    return render(request,'homepage.html')


@api_view(['GET'])
def add_blog(request):
    return render(request,'add_blog.html')

@api_view(['GET'])
def view_blog(request,blog_id):
    return render(request,'view_blog.html')

# class AddComment(APIView):
#     def post(self,request):


