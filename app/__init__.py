from flask import Flask


def create_app(config_class="Config"):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    #Load the configuration from config file
    app.config.from_object(f"config.{config_class}")

    from .views import views_bp as views_bp
    from .auth import auth as auth_bp

    app.register_blueprint(views_bp)


    return app

    
    

