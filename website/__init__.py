from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'ehehehe'
    app.config['UPLOAD_PATH'] = '../src/data_pdf/'

    from .views import views
    from .result import result

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(result, url_prefix='/')
    return app