# Internship

Project file name: sen

base url: 127.0.0.1:8000

command: python3 manage.py runserver

urls:

"" - for homepage

"admin/" - for admin page(username:abcd password:abcd)

"addsen" - for Sentry implementation

"threads" - for showing python threads

"additem" - for insertion operation with pymongo

"update" - for update operation with pymongo

"find" - for read operation with pymongo

"deletepost" - for delete operation with pymongo

"celtask" - for celery operation

In settings.py:

1)Included all the apps name in the list INSTALLED_APPS. 

2) Also included the details for implementing celery and sentry

For celery:

appname:celapp

1) created another file named tasks.py inside the app.

2) added 2 functions to check how celery works.

command:celery -A sen worker --loglevel=info

also we have to keep the redis server on for the celery task(command for redis server: redis-server)

Templates:

1)index.html: all the content for the home page

2) addpost.html: html file for inserting data in our databadse

3) read.html: html file for the read operation with mongodb

4) modify.html: html file that takes the key as input whose data has to modify

5) delete.html:html file that takes the key as input which has to delete from database
