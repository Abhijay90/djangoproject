from .models import *
from django.db import transaction


class Utility(object):
    def __init__(self):
        pass

    def to_list(self,queryset):
        # print queryset
        return [i for i in queryset]

    def to_dict(self,queryset):
        s = self.to_list(queryset)
        # print s
        if s:
            return {i:s[0][i] for i in s[0]}
        else:
            return {}

class BlogParagrahBase(Utility):

    def __init__(self):
        super(Utility,self).__init__()

    def addParagraph(self,blog_id,para):
        Paragraph.objects.create(blog_id = blog_id,content=para)

    def addParagraphComment(self,paragraph_id,comment):
        p = ParagraphComment.objects.create(paragraph_id = paragraph_id,comment=comment)
        p.save()
        return p.id

    def viewParagraphcomment(self,paragraph_id):
        s =  self.to_list(ParagraphComment.objects.filter(paragraph_id = paragraph_id).values())
        # print s
        return s

    def getAllBlogParagraph(self,blog_id):
        return self.to_list(Paragraph.objects.filter(blog_id = blog_id).values())




class BlogArticleBase(BlogParagrahBase):

    def __init__(self):
        super(BlogParagrahBase,self).__init__()

    def addBlog(self,title,content):
        try:
            with transaction.atomic():
                blog_id = self.__add_title(title)
                # print blog_id
                self.__create_paragraph_from_content(blog_id,content)
            transaction.commit()
            return dict(status = True,id = blog_id)
        except Exception as e:
            print e
            transaction.rollback()
            return dict(status=False)


    def __add_title(self,title):
        blog = Blog.objects.create(name=title)
        blog.save()
        return blog.id

    def __create_paragraph_from_content(self,blog_id,content):
        newline_position = content.find("\n\n")
        old_position=0
        while newline_position>0:
            # print newline_position
            self.addParagraph(blog_id=blog_id,para = content[old_position:newline_position-1])
            old_position=newline_position+2
            # print content[old_position:]
            newline_position = content[old_position:].find("\n\n")

        self.addParagraph(blog_id=blog_id,para = content[old_position:len(content)-1])

        # print "reached the end"

    def viewBlog(self,blog_id):
        b = self.to_dict(Blog.objects.filter(id = blog_id).values())
        # print b
        para = self.getAllBlogParagraph(blog_id)
        return dict(status=True,title = b["name"],paragraph = para)

    def viewBlogList(self):
        b = Blog.objects.all()
        return dict(status=True,data=self.to_list(b.values()))



class BlogCommentBase(BlogParagrahBase):
    def __init__(self):
        super(BlogParagrahBase,self).__init__()

    def addComment(self,paragraph_id,comment):
        try:
            comment_id =  self.addParagraphComment(paragraph_id=paragraph_id,comment=comment)
            return dict(status=True,id = comment_id)
        except Exception as e:
            return dict(status=False)

    def viewComment(self,paragraph_id):
        try:
            comment_list = self.viewParagraphcomment(paragraph_id=paragraph_id)
            # print comment_list
            return dict(status=True,comment_list=comment_list)
        except Exception as e:
            return dict(status=False)
