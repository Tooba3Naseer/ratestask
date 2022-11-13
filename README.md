# README

### Dependencies

1. Docker
2. Docker compose

### How do I get set up?

1. Clone the repository.
   `git clone <repository URL>`

2. Run the following command in order to create the images and build the container:
   `sudo docker-compose up --build`
   You can access the application by using this url http://127.0.0.1:1337.
   This command will take some minutes for the first time. Next time when you run the application, you don't
   need to build the container again. You can run the container using the command specified in point 3.

3. You can run the server by using following command:
   `sudo docker-compose up`
   (Now, you can access the application by using http://127.0.0.1:1337/ endpoint)

4. If you want to run any django management command, open up the bash for the ratestask-web container and run the management command there. Here are the commands for opening up the bash.

   1. `sudo docker ps -a` (List all containers)
   2. `sudo docker exec -it <container id of ratestask-web container> bash`

5. You can create the superuser for the admin portal by using following command:
   `python manage.py createsuperuser`
   After creating admin, you can login into the admin portal using that credentials. On admin portal, you can see the data in an interactive view.

6. If you have made any changes in requirements.txt or any docker configuration files. You need to create the images again by using the command that is specified in point 2.

### API Endpoint

This is the API endpoint:
http://127.0.0.1:1337/api/v1/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=baltic
You can call this endpoint from postman

### Who do I talk to, in case of any issues?

- toobanaseer3@gmail.com

### Additional information

1. Whenever you build the container for the first time using `sudo docker-compose up --build` command. It will automatically create postgres database along with web and nginx container. It will automatically run the database schema migration files and dump the data from json file into the database.

2. I used same data that you provided me. In Django, we generally dump the data from json file. So for this purpose I created json using this command, after running the container from the code that you provided me:
   `COPY (SELECT array_to_json(array_agg(row_to_json(t))) FROM (SELECT * FROM ports) t) to '/home/tooba/Desktop/result.json'`

3. Moreover, I attached the volumes so that the db data remains persist.
