from flask import Flask
from flask_migrate import Migrate
from src.config import Config
from src.db.core import db
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)
    app.config['JWT_SECRET_KEY']
    app.config['JWT_ACCESS_TOKEN_EXPIRES']
    jwt = JWTManager(app)

    # init db
    db.init_app(app)
    migrate = Migrate(app,db)

    with app.app_context():
        # import models first
        from src.db.models.users import Users
        from src.db.models.admin import Admin        # import blueprints
        from src.api.resources.users import users_bp
        from src.api.resources.admin import admin_bp
        from src.api.models.admin_sales import admin_sales_bp
        from src.api.models.users_sales import users_sales_bp
        from src.api.models.pricing import pricing_bp
        from src.api.models.login_forms import login_bp
        from src.api.models.records import records_bp

        # register blueprints
        app.register_blueprint(users_bp)
        app.register_blueprint(admin_bp)
        app.register_blueprint(admin_sales_bp)
        app.register_blueprint(users_sales_bp)
        app.register_blueprint(pricing_bp)
        app.register_blueprint(login_bp)
        app.register_blueprint(records_bp)

    
    
    return app
app = create_app()

if __name__=="__main__":
    app.run(debug=True)
    