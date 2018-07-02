Setup:

Recommended install in virtual environment

to install run 

sh setup.sh


python manage.py runserver



Description:


Initial Url:

http://127.0.0.1:8000/hompage


APIs:

1./add_blog_api

Gives list of all blogs

2. view_blog_api/<blog_id>

give blog data

3. comment_api/<paragraph_id>

GET:
	give comment list to particular paragraph

POST:

	Post comment on a particlar paragraph

URLS:
/homepage/

list all blogs available

/view-blog/<blog_id>

show selected blog

/add-blog/

creates blog


Requirement:

python 2.7
django 1.11
djangorestframework






