import os
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config["SECRET_KEY"]='6f56672ccb1390ca03e65311b682459a'
    
    
    '''
    	the register_bluerprint method is used 
    	to allow other modules to use the app instance
    '''
    from . import main, processes
    app.register_blueprint(main.mainApp)
    app.register_blueprint(processes.processesApp)

    return app
