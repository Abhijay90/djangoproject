from .models import *

class BlogParagrahBase(object):

	def __init__(self):
		pass

	def addParagraph(self):
		pass

	def addParagraphComment(self,paragraph_id):
		pass

	def viewParagraph(self,paragraph_id):
		pass

	def viewParagraphcomment(self,paragraph_id):
		pass


class BlogArticleBase(BlogParagrahBase):

	def __init__(self):
		pass

	def addBlog(self):
		pass

	def __add_title(self,title):
		pass

	def __add_paragraph(self,para):
		pass

	def viewBlog(self,id):
		pass

	def viewBlogList(self):
		pass



class BlogCommentBase(BlogParagrahBase):
	def __init__(self):
		pass

	def addComment(self,paragraph_id):
		pass

	def viewComment(self,paragraph_id):
		pass
