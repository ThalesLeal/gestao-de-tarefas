from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)  # Adicionando CORS à aplicação

    from app.routes import bp as routes_bp  # Importa o blueprint das rotas
    app.register_blueprint(routes_bp)

    return app
