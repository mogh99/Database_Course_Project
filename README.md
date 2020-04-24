DON'T FORGET TO RUN THE VIRTUAL ENVIROMENT BEFORE RUNING THE APPLICATION:
1. to activiate the enviroment
$ source env/bin/activate
2. to deactivate the enviroment
(env) $ deactivate


To run the flask server:
1. go to the ICS343Project folder
2. export FLASK_APP=run.py
3. export FLASK_ENV=development
4. flask run

To create the database open python shell in the terminal:
>>> from application import db, create_app
>>> db.create_all(app=create_app())

runing the db.create_all() without the app will cause the error:
RuntimeError: No application found. Either work inside a view function or push an application context. See http://flask-sqlalchemy.pocoo.org/contexts/.
