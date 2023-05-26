from flask import Flask, config
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    from app.main import bp as main_blueprint
    from app.post import bp as post_blueprint
    from app.categorias import bp as categorias_blueprint
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(post_blueprint, url_prefix="/post")
    app.register_blueprint(categorias_blueprint, url_prefix="/categorias")
    
    @app.route("/ping")
    def ping(): 
        return "sirve"

    return app