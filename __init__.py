from flask import Flask
from env.config import Config
from database import init_db
from routes.user_routes import user_bp

def create_app():
    app = Flask(__name__);
    app.config.from_object(Config);
    
    init_db(app);

    app.register_blueprint(user_bp);
    return app;
