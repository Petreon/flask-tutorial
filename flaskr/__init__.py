import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True) ## creates the flask instance
    ## __name__ is the name of the current Pyhton module, the app needs to know where it's located to set up some paths
    ## and __name__ is a convenient way to tell it that

    ## instance_relative_config=True, tells that configurations files are relative(depends) the instance folder

    app.config.from_mapping( ## sets some default configurations that the app will use
        SECRET_KEY='dev', ##is used like a key to keep data safe, in deployment it needs to be a radon value
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), ## its where SQlite database file will be save, future this will be explained better
    )



    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
        #overrides the default configuration with values taken from the config.py file in the instance folder if it exists. For example, when deploying, this can be used to set a real SECRET_KEY.

        #test_config can also be passed to the factory, and will be used instead of the instance configuration. This is so the tests you’ll write later in the tutorial can be configured independently of any development values you have configured.

    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
        #os.makedirs() ensures that app.instance_path exists. Flask doesn’t create the instance folder automatically, but it needs to be created because your project will create the SQLite database file there.
    except OSError:
        pass

    # a simple page that says hello

    @app.route("/hello")
    def hello():
        return "Hello, World!"
    #@app.route() creates a simple route so you can see the application working before getting into the rest of the tutorial. It creates a connection between the URL /hello and a function that returns a response, the string 'Hello, World!' in this case.
    
    return app

#flask --app flaskr run --debug