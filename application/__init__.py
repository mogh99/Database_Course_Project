from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    
    '''
    	the register_bluerprint method is used 
    	to allow other modules to use the app instance
    '''
    from application.main.main import mainApp
    from application.main.processes import processesMainApp
    from application.admin.admin import adminApp
    from application.admin.processes import processesAdminApp
    app.register_blueprint(mainApp)
    app.register_blueprint(processesMainApp)
    app.register_blueprint(adminApp)
    app.register_blueprint(processesAdminApp)

    return app
