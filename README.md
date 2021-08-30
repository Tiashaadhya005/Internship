# Internship

Description: this project file includes implementations of custome model manager, sentry , celery, threads etc.

base url: 127.0.0.1:8000

command: python3 manage.py runserver

urls:

"admin/" - this url opens admin page . here we have to login into the admin page using userid and password . where Userid :abcd and password:abcd


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

6) index_reg_log.html: html file that gives the option for register/login(this is for the implementation of custom model manager)

7) regisater.html: html file for the registration (this is for the implementation of custom model manager)

8) login.html:html file for login (this is for the implementation of custom model manager)

9) show.html: html file for showing all the data from database
