# About the Term Project
This is the term project for the database course. The course focuses on the database design and who to create efficient models.
The project requirements were to build a program (Desktop application, mobile application, or anything) that shows the data of a tournament.
The tournament has multiple teams and matches. Every team consists of multiple players from different departments and positions. The main goal of the
project is to build a database in the most efficient way and display the data.

## Our Project
Every team consists of three members. Our team decides to build a website for the term project and different technologies were used to accomplish the task. The front end was built using bootstrap studio which is an application help in constructing the front end. Flask, Jinja, WTF-Forms, and SQLAlchemy were used for completing the backend. SQLit was used for the database because we want something light and easy for fast testing.

### Run the Application Locally
1. Download the repository in your preferred location
```
~$ git clone https://github.com/mogh99/Database_Course_Project.git
```
2. Install all the required dependincies other than python3
```
~$ pip3 install -r requirements.txt
```  
3. Run the application
```
~$ python3 run.py
```
OR Insted of step 3
```
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

### Create the Database
To create the database open python shell in the terminal:
1. import all the dependincies
```
>>> from application import db, create_app
>>> from application.models import * 
```
2. create the app and push the context
```
>>> create_app().app_context().push()
```
3. create the database
```
>>> db.create_all()
```
**Note**:these step will create the database in the application folder. This can be changed from the config.py file.
