from flask import Flask


def create_app():
    app = Flask(__name__)
    with app.app_context():
        from . import routes

        app.register_blueprint(routes.bp)
    return app

def run():
   while run.debug : True
with create_app.run():
    from . import routes
    routes.convert_url_to_mp3(tuple[object:"audio/mp3"])