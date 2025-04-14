from flask import Flask
from flask_cors import CORS
from api.routes import portfolio_bp

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes
    
    # Register blueprints
    app.register_blueprint(portfolio_bp)
    
    return app