# Internship

Description: this project file includes implementations of custome model manager, sentry , celery, threads etc.


urls:

"admin/" - this url opens admin page . here we have to login into the admin page using userid and password . where Userid :abcd and password:abcd


For celery:

appname:celapp

1) created another file named tasks.py inside the app.

2) added 2 functions to check how celery works.


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


now to execute the project --

1) first we need to pull this from git.

2)Then we have to install docker 

3)Now we have to go to the selected folder and have to run the command 
`docker
docker-compose build` 
to build the image of the project 

4) Next we have to run `docker-compose up` to make the container and to start the docker server.

5) For checking the container we can run the command `docker ps`. It will show all the containers that are running. 
   Also we can check any container that was build and then exited by using `docker ps -a`.
   
6) Now we can check the operations in the browser. 

7) At last to stop the docker we will run 
    `docker-compose kill` .

8) then again we can run `docker ps` to verify whether all the containers deleted or not.
