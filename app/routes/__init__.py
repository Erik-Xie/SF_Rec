from .home import home_bp
from .about import about_bp
from .feature import feature_bp
from .recommendation import recommendation_bp

def register_routes(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(feature_bp)
    app.register_blueprint(recommendation_bp)


