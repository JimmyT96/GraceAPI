from flask import Flask

def create_app():
    app = Flask(_name_)
    from app.routes import bp
    app.register_blueprint(bp)
    return app


